import uuid

import aredis

# import asyncio
import json


class NLUQueue(object):
    def __init__(self, name, namespace='queue', **redis_kwargs):
        # redis的默认参数为：host='localhost', port=6379, db=0， 其中db为定义redis database的数量
        redis_kwargs["host"] = "redis"
        self.__client = aredis.StrictRedis(**redis_kwargs)
        self.key = '%s:%s' % (namespace, name)

    async def qsize(self):
        return await self.__client.llen(self.key)  # 返回队列里面list内元素的数量

    async def enqueue(self, item):
        await self.__client.rpush(self.key, item)  # 添加新元素到队列最右方

    # def get_wait(self, timeout=None):

    async def dequeue_nowait(self):
        # 直接返回队列第一个元素，如果队列为空返回的是None
        item = await self.__client.lpop(self.key)
        message = item.decode("utf-8") if item is not None else None
        # message = json.loads(message.decode("utf-8"))
        return message

    async def set_msg_by_direct_id_ex(self, id, second2expire, value):
        await self.__client.setex(id, second2expire, value)  # set message by direct id

    async def get_msg_by_direct_id(self, id):
        item = await self.__client.get(id)  # get message by direct id
        if item:
            item = item.decode("utf-8")
        return item


class QueueRequestTask(object):
    def __init__(self, data, task_type_label, to_worker_queue_name="to_worker", to_master_queue_name="to_master"):
        self.task_uuid = str(uuid.uuid4())
        self.data: dict = data
        self.to_worker_queue = NLUQueue(name=to_worker_queue_name, namespace=task_type_label)
        self.to_master_queue = NLUQueue(name=to_master_queue_name, namespace=task_type_label)

    async def to_worker(self):
        data = {
            "obj": self.data,
            "request_id": self.task_uuid
        }
        print(f"data: {data}")
        task_str = json.dumps(data, ensure_ascii=False)
        await self.to_worker_queue.enqueue(task_str)

    async def get_content(self):
        res = await self.to_master_queue.get_msg_by_direct_id(self.task_uuid)
        return res


class QueueRespondsTask(object):
    def __init__(self, task_type_label, to_worker_queue_name="to_worker", to_master_queue_name="to_master"):
        self.to_worker_queue = NLUQueue(name=to_worker_queue_name, namespace=task_type_label)
        self.to_master_queue = NLUQueue(name=to_master_queue_name, namespace=task_type_label)

    async def to_master(self, obj, request_id):
        # obj["worker"] = task_name
        print(f"send_responds: {obj}")
        return_value = json.dumps(obj, ensure_ascii=False)
        return await self.to_master_queue.set_msg_by_direct_id_ex(id=request_id, second2expire=300, value=return_value)

    async def get_content(self):
        res = await self.to_worker_queue.dequeue_nowait()
        res = json.loads(res) if res is not None else None
        return res