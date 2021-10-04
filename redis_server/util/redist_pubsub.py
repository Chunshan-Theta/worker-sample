import redis


class NLUPublish(object):
    def __init__(self, channel, **redis_kwargs):
        # redis的默认参数为：host='localhost', port=6379, db=0， 其中db为定义redis database的数量
        self.__db = redis.Redis(**redis_kwargs)
        self._channel = channel  # '%s:%s' % (namespace, name)

    def publish(self, item):
        self.__db.publish(
            self._channel,
            item,
        )


class NLUSubscribe(object):
    def __init__(self, channel, **redis_kwargs):
        # redis的默认参数为：host='localhost', port=6379, db=0， 其中db为定义redis database的数量
        self.__db = redis.Redis(**redis_kwargs)
        self._channel = channel  # '%s:%s' % (namespace, name)

        self.__sub = self.__db.pubsub()
        self.__sub.subscribe(self._channel)

    def listen_messages(self):
        return self.__sub.listen()

    def unsubscribe(self):
        self.__sub.unsubscribe(self._channel)