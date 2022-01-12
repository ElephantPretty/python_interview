import redis

poll = redis.ConnectionPool(host='localhost', port=6379,decode_responses=True)
r = redis.StrictRedis(connection_pool=poll)#课程是redis.StrictRedis(connection_pool=poll) 我改为StrictRedis

# https://www.bilibili.com/video/BV16N411R7VN?p=6
def string_test():
    """
    操作string
    def set(
        self,
        name,--redis的key
        value,--redis的value
        ex=None,--失效时间,单位秒
        px=None,--失效时间,单位毫秒
        nx=False,--nx=True->当name不存在时插入
        xx=False,--xx=True->当name存在时插入
        keepttl=False,
        get=False,
        exat=None,
        pxat=None,
    ):
    :return:
    """
    # r.set('username', 'zhangsan', ex=5)
    # r.set('username', 'zhangsan')
    # name不存在时插入，也就是key不存在时插入，但此时里面已经有zhangsan了，显然lisi无法插入
    # r.set('username', 'lisi', nx=True)
    # r.set('user', 'lisi', nx=True) #可插入 因为换了一个name
    # r.set('username', 'lisi1', xx=True) # name,即key，存在时可以插入，这是xx=True的作用
    # print(r.get('username'))
    # 1 ex过期时间5s
    r.set('username', 'zhangsan', ex=5)
    print(r.get('username'))
    # 2 px过期时间5ms
    r.set('username', 'zhangsan', px=5)
    print(r.get('username'))
    # 3 nx如果key-username不存在，那么输出True;如果username-key已经存在，输出是None--key存在不会覆盖
    print(r.set('username','zhangsan',nx=True))
    # 4 xx如果key-username已经存在，那么输出是True;如果key-username不存在啊，输出是None--key存在会覆盖
    print(r.set('username','lisi2',xx=True))
    # 5 setnx(name, value)------------------想想nx,直接setnx，效果一样
    # 设置值，只有name不存在时，执行设置操作（添加）--这个操作效果是避免重复添加key值--实际应用呢？
    print(r.setnx('username2', 'zhangsan'))
    # 6 setex----直接设置过期时间--这点和视频中不一致，参数顺序改了
    # (name, time, value)
    r.setex("username",5, "zhangsan" )
    print(r.get('username'))
    # 7 psetex---5000ms后过期
    r.psetex('username', 5000, "zhangsan")
    print(r.get("username"))
    # 8 mset--批量设置值--传一个字典,视频中另外一种方式错误
    r.mset({'k1':'v1','k2':'v2','k3':'v3'})
    # 9 mget--批量获取
    print(r.mget('k1','k2','k3'))# 一次取出多个键对应的值
    print(r.mget(['k1','k2','k3']))# 一次取出多个键对应的值
    print(r.mget('k1'))
    # 10 先拿到之前的值-zhangsan，在用lisi覆盖--感觉可能不常用
    print(r.getset("username", "lisi"))
    """
    11
    getrange(key, start, end)
    获取子序列(根据字节获取,非字符)
    参数:name
    start-起始位置（字节）
    end-结束位置(字节)
    如，"商还尚学堂",0-3表示"上"
    字符串类型是Redis中最为基础的数据存储类型，
    是一个由字节组成的序列，他在Redis中是二进制安全的，
    """
    r.set("cn_shsxt", "上海尚学堂")
    print(r.getrange("cn_shsxt", 0, 2)) # 一个汉字占3个字节，cli下可用strlen cn_shsxt查看
    print(r.getrange("cn_shsxt", 0, -1))
    r.set("en_shsxt", "shsxt")# 字母
    print(r.getrange("en_shsxt", 0, 2))# 一个英文字母占1个字节
    print(r.getrange("en_shsxt", 0, -1))
    """
    12 setrange(name,offset,value)
    修改字符串内容，从指定字符串索引开始向后替换(新值太长时，则向后添加)
    offset,字符串的索引,字节(一个汉字三个字节)
    value,要设置的值
    """
    r.setrange("en_shsxt", 0, "bj") #r.setrange("en_shsxt", 0, "bj11111111111") 北京字节是6，直接全替换
    print(r.get("en_shsxt"))
    # 13 strlen(name) 返回name对应的字节长度(一个汉字3个字节)
    print(r.strlen("en_shsxt"))
    """
    incr(self, name, amount=1)
    自增 name对应的值，
    当name不存在时，则创建name=amount,否则，则自增
    参数:name,redis的name
    amount,自增数(必须是整数)
    注:同incrby
    """
    r.set("foo", 123)#值是123 不是字符串！
    print(r.strlen("foo"))#3,虽说我们看起来是个int型，但存储还是按照字节来存的
    print(r.mget("foo"))
    r.incr("foo", amount=1)
    print(r.mget("foo"))
    """
    自增应用场景-页面点击数
    假定我们对一系列页面都需要记录点击次数，
    假如论坛的每个帖子都需要点击次数，而点击次数比回帖的次数多得多。
    如果使用关系型数据库来存储点击，可能存在大量行级锁争用。
    所以，点击数的增加使用redis的INCR命令最好不过了。
    当redis服务器启动时,可以从关系数据库读入点击数的初始值
    (12306这个页面被访问34634次)
    -----------------------------------------------
    1-什么是锁？我们以InnoDB存储引擎为例子
    锁定用于确保事务完整性和数据库一致性。 锁定可以防止用户读取其他用户正在更改的数据，
    并防止多个用户同时更改相同的数据。 如果不使用锁定，
    数据库中的数据可能在逻辑上变得不正确，而针对这些数据进行查询可能会产生想不到的结果。
    2-为什么要用锁？
　　在计算机科学中，锁是在执行多线程时用于强行限制资源访问的同步机制，
    即用于在并发控制中保证对互斥要求的满足。在数据库的锁机制中介绍过，
    在DBMS中，可以按照锁的粒度把数据库锁分为行级锁(INNODB引擎)、表级锁(MYISAM引擎)和页级锁(BDB引擎 )。
    InnoDB存储引擎既支持行级锁（ row-level locking），
    也支持表级锁，但默认情况下是采用行级锁。
    3-行级锁
    行级锁是Mysql中锁定粒度最细的一种锁，表示只针对当前操作的行进行加锁。
    行级锁能大大减少数据库操作的冲突。
    其加锁粒度最小，但加锁的开销也最大。行级锁分为共享锁 和 排他锁。
    特点
　　开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高。
    -----------------------------------------------目前没加过，也未练习过类似的，留待数据库学习研究
    """
    r.set("visit:12306:totals", 34634)
    print(r.get("visit:12306:totals"))
    # 每当有一个页面点击，则使用INCR增加点击数即可
    r.incr("visit:12306:totals")# 这是redis提供的一种以目录层级来存放数据的方式
    r.incrby("visit:12306:totals")
    # 页面载入的时候可直接获取这个值
    print(r.get("visit:12306:totals"))
    # r.delete("visir:12306:totals")
    """
    15 
    incrbyfloat(self, name, amount=1.0)
    自增 name对应的值,当name不存在时，则创建name=amount,否则，则自增
    参数:
    name,redis的name
    amount,自增数(浮点型)
    """
    r.set("foo1", "123.0")
    r.set("foo2", "221.0")
    print(r.mget("foo1", "foo2"))
    r.incrbyfloat("foo1", amount=2.5)
    r.incrbyfloat("foo2", amount=3.0)
    print(r.mget("foo1", "foo2"))
    """
    16
    decr(self, name, amount=1)
    自减 name对应的值，当name不存在时,则创建name=amount,
    否则，则自减
    参数,redis的name, amount,自减数(整数)
    """
    r.set('foo4', 5)
    r.decr("foo4", amount=3)
    print(r.mget("foo1", "foo4"))
    """
    17 append(key, value)
    value-要追加的字符串
    """
    r.append("username", "haha") #在name对应的值lisi后面追加字符串haha
    print(r.mget("username"))
    # 常用的17个------花费1-2h【效率比较低的一天】


def hash_test():





def tmp_test():
    # string_test()

    pass


if __name__ == "__main__":
    tmp_test()