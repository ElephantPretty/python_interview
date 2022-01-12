import redis


def init01():
    """
    通过redis对象连接服务器
    不推荐使用redis，使用StrictRedis好一点
    :return:
    """
    # decode_responses=True时存字符串，decode_responses=False时存入字节，
    # 我的redis未设置密码，不需要password
    r = redis.Redis(host='localhost', port=6379,decode_responses=True)
    print(r.ping())# True


def init02():
    """
    通过连接池获取redis对象连接服务器
    在python3中redis连接包读取数据默认返回byte类型。存进去的是字符串类型的数据，取出来却是字节类型的。
    cli get username ----"\xe5\xbc\xa0\xe4\xb8\x89"
    假若是set("username", "zhangsan")----则cli为"zhangsan"
    无论是中文还是英文，从图形化redis无法区分
    :return:
    """
    # 拿到一个连接池
    poll = redis.ConnectionPool(host='localhost', port=6379,decode_responses=False)
    r = redis.Redis(connection_pool=poll)
    print(r.ping())
    r.set('username', '张三')
    print(type(r.get('username')))
    print(r.get('username'))
    # 手动释放连接-----没必要写
    # r.connection_pool.disconnect()

if __name__ == '__main__':
    init02()



