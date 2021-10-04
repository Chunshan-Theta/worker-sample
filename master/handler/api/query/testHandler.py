import json

from handler.api.apiHandlerBase import APIHandlerBase
from util.aredis_queue import QueueRequestTask
import asyncio
class testHandler(APIHandlerBase):

    async def get(self):
        """
        ---
        tags:
        - Posts
        summary: List posts
        description: List all posts in feed
        produces:
        - application/json
        responses:
            200:
              description: test
        """
        task_data = {
            "re": "hello"
        }
        Task = QueueRequestTask(data=task_data, task_type_label="test")

        #
        await Task.to_worker()

        #
        worker_response = await Task.get_content()
        time = 0
        while worker_response is None and time < 500:
            worker_response = await Task.get_content()
            time += 1
            await asyncio.sleep(0.1)
        else:
            return self.write_json({
                'get parameter': task_data,
                "worker response": json.loads(worker_response)
            })

