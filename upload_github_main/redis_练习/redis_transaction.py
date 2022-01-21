import redis
poll = redis.ConnectionPool(host='localhost', port=6379,decode_responses=True)
r = redis.Redis(connection_pool=poll)


def transaction_test():
    """操作事物
    redis实际中只需要就考虑缓存如何实现，
    事物主要是从mysql这方面去考虑
    """
    try:
        pipe = r.pipeline(transaction=True) # 默认启用事物
        pipe.multi() # 开启事物
        pipe.set('username', 'zhangsan')
        pipe.hmset("hash2", {"user": "zhangsan", "sex": 1})
        pipe.sadd('letters', 'a', 'b', 'c')
        """
        管道的命令可以写在一起
        """
        pipe.set('username','zhangsan').hset('user','username','lisi').sadd('letters','a','b').execute()
        pipe.execute() # 提交事物
        1 / 0 # 异常
        pipe.execute() # 提交事物
    except Exception as e:
        pipe.reset()  # 回滚事物
        print(e)
        print('回滚成功')
        pass


if __name__ == '__main__':
    transaction_test()