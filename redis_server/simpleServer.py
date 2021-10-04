from time import sleep
from util.redis_queue import NLUQueue
import redis
import json


def main():
    q = NLUQueue(name="nlumdl1-eryuij345236sfdagete-wk1", namespace="localhost:6379")
    idx = 1
    # init model
    while True:

        retStr = q.dequeue_nowait()
        if retStr:
            print(idx,"queue size: ",q.qsize())
            print ("Get:" + retStr)
            arr_q_msg = retStr.split(chr(9)+"|")
            print ("Content:",arr_q_msg)
            print ("Pushed:", arr_q_msg[4], arr_q_msg[0])
            push2queue_Msg(q, arr_q_msg[4], arr_q_msg[0])
            idx += 1
        else:
            if q.qsize() == 0:
                sleep(0.01)
            else:
                pass


def push2queue_Msg(q, mid, content, time=120):
    q.setMsgByIdEx(mid, time, json.dumps({"content": content}))


r = redis.Redis(host='localhost', port=6379, db=0)


def push2queue_channel(q, mid, content):
    global r
    r.publish(mid, content)


if __name__ == "__main__":
    main()
