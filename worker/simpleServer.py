import os
from util.aredis_queue import QueueRespondsTask
import asyncio


async def main():

    while True:
        print(f"Get Works.....")
        QRTask = QueueRespondsTask(task_name)
        task = await QRTask.get_content()
        if task is None:
            await asyncio.sleep(1)
            continue

        #
        obj = task.get("obj", None)
        request_id = task.get("request_id", None)


        #
        await QRTask.to_master({
            "obj": obj,
            "from": "worker"
        }, request_id)


task_name = os.getenv("task_name", "default")
print(f"Get work from: {task_name}")
asyncio.run(main())
