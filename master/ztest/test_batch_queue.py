import random
import time
import uuid

from tornado.testing import AsyncTestCase, gen_test

from util import tools
from util.aredis_queue import *


class TestBatchMode(AsyncTestCase):
    """Test Util nlu_queue_asyn"""

    # 為了解決
    # 1. 一個batch 大量的query 阻塞服務
    # 2. 提高worker 效率
    # 3. 保持 LB and Failover

    # 錯誤處理
    # 1. 單句 worker 錯誤回應
    # 2. worker timeout
    # 3. redis error( connection error and redis timeout)
    async def batch_query_2_worker(self, query_str_arry):

        # 1. receive a list of query sentences (query_str_arry)
        # 2. enqueue max N sentences to queue and keep ID in lst_query_uuid
        # 3. check and receive responses (by get_msg_by_direct_id) in lst_query_uuid from worker
        # 4. until waiting sentences in list (lst_query_uuid) less than N/2, enqueue next N - len(lst_query_uuid) sents
        # 5. finish request if all query sentences enqueue and get all response back from workers
        # Note: expired time, log and error handling not included
        # N = model_batch_size * workers * 2

        # define parameters
        return_redis_ip = ''
        return_redis_port = ''

        # number of batch size in model setting
        model_batch_size = 16
        worker_nbr = 2

        # nlu_queue for enqueue to model worker
        # nlu_queue_result for getting result from model wokrer
        self.nlu_queue = nlu_queue_asyn('test')
        self.nlu_queue_result = nlu_queue_asyn('result')

        # control number of max sentences in queue
        # suggest we set model_batch_size * workers * 2
        max_release_2_queue_nbr = model_batch_size * worker_nbr * 2

        curr_idx = 0
        lst_query_uuid = list()
        dict_uuid_result = dict()
        dict_sent_uuid = dict()
        query_len = len(query_str_arry)

        print("Sentences to 2 be process:", query_len)
        print("max_release_2_queue_nbr:", max_release_2_queue_nbr)
        while True:

            # Check result from model workers
            while True:
                # no records to be checked, break
                if len(lst_query_uuid) == 0:
                    break

                tmp_list = lst_query_uuid.copy()
                # try to fetch all results of uuid in lst_query_uuid
                for uuid_key in tmp_list:
                    # mock a random response from the worker in testing
                    # TO BE REMOVED in api handler
                    if random.randint(0, 100) > 50:  # 50% of the chance having a result
                        await self.nlu_queue.set_msg_by_direct_id_ex(uuid_key, 30, "response of " + uuid_key)

                    # get responds from queue by key.
                    retStr = await self.nlu_queue_result.get_msg_by_direct_id(uuid_key)

                    # confirmed the responds is ready
                    if retStr is not None:
                        # Save results
                        # print("5:Key: {} is {}".format(uuid_key, retStr))
                        dict_uuid_result[uuid_key] = retStr
                        lst_query_uuid.remove(uuid_key)

                    # add queue error handling here

                # if lst_query_uuid has items less than half of the required qty
                if len(lst_query_uuid) < (max_release_2_queue_nbr / 2) and curr_idx < query_len:
                    break

            # if current index greater total query length (all query result released and collected) , break and finish
            # print("EXIT Check curr_idx:{} query_len:{}".format( curr_idx, query_len))

            if curr_idx >= query_len:
                break

            # enqueue query to queue (with max_release_2_queue_nbr limit)
            for idx in range(curr_idx, curr_idx + max_release_2_queue_nbr - len(lst_query_uuid)):
                if idx >= query_len:
                    break
                # push to queue to RANDOM queue,
                # TO BE IMPLEMENTED in api handler
                #         user_servers = random.choice(self.configs[service_token].servers)
                #         user_workers = user_servers.workers
                #         worker = random.choice(user_workers)
                tmp_id = str(uuid.uuid4())
                # print ("Encode idx:" , idx , query_len)
                content = tools.encode_api_msg_2_worker(mq_ip=return_redis_ip, mq_port=return_redis_port,
                                                        msg=query_str_arry[idx],
                                                        req_uuid=tmp_id)
                # self.logger.debug("qsize: " + str(await myQ_remote.qsize()))
                await self.nlu_queue.enqueue(content)

                # append tmp_id to waiting list and keep sent and uuid mapping
                lst_query_uuid.append(tmp_id)
                dict_sent_uuid[query_str_arry[idx]] = tmp_id

                # remove item from queue right away to mock worker read this message
                # TO BE REMOVED in api handler
                retmsg = await self.nlu_queue.dequeue_nowait()

            curr_idx = idx

        del self.nlu_queue
        del self.nlu_queue_result

        return [(sent, dict_uuid_result[dict_sent_uuid[sent]]) for sent in query_str_arry]

    @gen_test(timeout=20)
    def test_batch_query(self):

        file_path = './test_sample/全部句子.txt'
        with open(file_path, 'r') as fin:
            arr_sent = fin.readlines()

        # Test 3 random number (sample_cnt) of query
        for test_cnt in range(0, 3):
            time_start = time.time()
            sample_cnt = random.randint(10, 1000)

            arr_q_sent = random.choices(arr_sent, k=sample_cnt)

            print(" === Test {} , Sample Cnt {} === ".format(test_cnt, sample_cnt))

            result = yield self.batch_query_2_worker(arr_q_sent)

            test_error = 0
            if len(result) != sample_cnt:
                print("Return Result Count {} Error ! ".format(len(result)))
                test_error += 1

            for q_idx in range(0, len(arr_q_sent)):
                if result[q_idx][0] != arr_q_sent[q_idx]:
                    print("ERROR found:{} , {}".format(q_idx, result[q_idx][0]))
                    test_error += 1

            print("Process time {} ".format(time.time() - time_start))

            self.assertEqual(0, test_error)
