import redis
# https://www.bilibili.com/video/BV16N411R7VN?p=6 学习资料

poll = redis.ConnectionPool(host='localhost', port=6379,decode_responses=True)
r = redis.StrictRedis(connection_pool=poll)#课程是redis.Redis(connection_pool=poll) 我改为StrictRedis

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
    """
    操作hash
    1-hset--单个增加--修改(单个取出)--没有就新增，有的话就修改
    hset(name, key, value)
    name对应的hash中设置一个键值对(不存在，则创建;否则，修改)
    参数:
    name,redis的name
    key,对应的hash中的key
    value,对应的hash中的value
    注释:hsetnx(name, key, value)当name对应的hash中不存在当前key时则创建(相当于添加)
    :return:
    """
    r.hset("hash1", "k1", "v1") # redis的key hash的key hash的value
    r.hset("hash1", "k1", "v11")
    r.hset("hash1", "k2", "v2")
    print(r.hkeys("hash1"))# 取hash中所有的key
    print(r.hget("hash1", "k1"))# 单个取hash的key对应的值
    print(r.hmget("hash1", "k1", "k2"))# 多个取hash的key对应的值
    # nx如果键不存在,那么输出是1;如果键已经存在,输出是0---使用要求是如果不存在，才插入,若存在则操作无效
    print(r.hsetnx("hash1", "k5", "v3"))
    print(r.hget("hash1", "k2"))
    """
    2 批量增加(取出)
    hmset(name, mapping)
    在name对应的hash中批量设置键值对
    参数:
    name,redis的name
    mapping,字典，如{'k1':'v1','k2':'v2'}
    弃用通知：从 Redis 版本 4.0.0 开始，
    此命令被视为已弃用。虽然不太可能完全删除它，
    但更喜欢使用具有多个字段值对的"HSET"来代替它。
    https://redis.io/commands/hmset
    我的实验redis版本是3.2.100 还不支持hset多个插入
    """
    r.hmset("hash2", {"k2":"v2","k3":"v3"})
    # r.hset("hash22","k1","v1")
    # r.hset("hash22", {"k1","v1","k2","v2"})
    """
    hget()
    hmget(name,keys,*args)----*args，要获取的key，如k1,k2,k3
    keys 要获取的key集合,如['k1', 'k2', 'k3']
    *args 要获取的key,如:k1,k2,k3
    """
    print("11111", r.hget("hash2", "k2")) # 单个取出"hash2"的key-k2对应的value
    print(r.hmget("hash2", "k2", "k3")) # 批量取出"hash2"的key-k2 k3对应的value--方式1
    print(r.hmget("hash2", ["k2", "k3"])) # 批量取出hash2"的key-k2 k3对应的value--方式2
    """
    3-取出所有的键值对
    hgetall(name)
    获取name对应hash的所有键值
    """
    print(r.hgetall("hash1"))
    """
    4-得到所有键值对的hash长度
    hlen(name)
    获取name对应的hash中键值对的个数
    """
    print(r.hlen("hash1"))
    """
    5-得到所有的keys（类似于字典的取所有keys）
    hkeys(name)
    获取name对应的hash中所有的key值
    """
    print(r.hkeys("hash1"))
    """
    6-得到所有的value，类似于字典的取所有value
    hvals(name)
    获取name对应的hash中所有的value的值
    """
    print(r.hvals("hash1"))
    """
    7-判断成员是否存在(类似字典的in)
    hexists,检查name对应的hash是否存在当前传入的key
    """
    print(r.hexists("hash1", "k4"))# False 不存在
    print(r.hexists("hash1", "k1"))# True 存在
    """
    8-自增自减整数(将key对应的value--证书 自增1或2或者别的整数 负数就是自减)
    hincrby(name, key, amount=1)
    自增name对应的hash中的指定key的值不存在则创建key=amount
    name-redis中的name
    key-hash中的key
    amount-自增数(整数)
    """
    r.hset("hash1", "k4", 123)
    r.hincrby("hash1", "k4", amount=-1)
    print(r.hgetall("hash1"))
    r.hincrby("hash1", "k6", amount=1) #不存在的话,value默认为1
    print(r.hgetall("hash1"))
    """
    9-自增自减浮点数(将key对应的value--浮点数 自增1.0或2.0)
    hincrbyfloat(name, key, amount=1.0)
    自增name对应的hash中的指定key的值，不存在则创建key=amount
    """
    r.hset("hash1", "k5", "1.0")
    r.hincrbyfloat("hash1", "k5", amount=-1.0)# 已存在,递减-1.0
    print(r.hgetall("hash1"))
    r.hincrbyfloat("hash1", "k7", amount=-1.0)# 不存在,value初始值是-1.0,每次递减1.0
    print(r.hgetall("hash1"))
    """
    10-删除键值对
    hdel(name, *keys)-删除一个键值对
    """
    print(r.hgetall("hash1"))
    r.hdel("hash1", "k1")
    print(r.hgetall("hash1"))
    """
    hsacn_iter(name, match=None, count=None)
    利用yield封装hscan创建生成器,实现分批去redis中获取数据
    match-匹配指定key,默认None，表示所有的key
    count-每次分片最少获取个数,默认None表示采用redis的默认分片个数
    """
    for item in r.hscan_iter("hash1"):
        # 获取所有key，进行迭代
        print(item)
    print(r.hscan_iter("hash1")) #生成器内存地址
    print(r.hscan("hash1"))# 获取所有hash数据 hscan(self, name, cursor=0, match=None, count=None)
    # 1-1.5h 效率可以


def list_test():
    """
    操作list
    1-增加(类似于list的append,只是这里从左边新增加)--没有就新建
    lpush(name, values),在name对于的list中添加元素，每个新的元素都添加到列表的最左边
    :return:
    """
    r.lpush("list1", 11, 22, 33)
    print(r.lrange('list1', 0, -1))
    # 2-增加(从右边增加)--没有就新建
    r.rpush("list2", 44, 55, 66) # 在列表的右边，依次添加44,55,66
    print(r.llen("list2"))# 列表长度
    print(r.lrange("list2", 0, -1)) # 切片取出值，索引号0到-1(最后一个元素)
    """
    3.往已经有的name的列表的左边添加元素，没有的话无法创建
    lpushx(name, value)
    在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
    """
    r.lpushx("list10", 10) # 这里list10不存在
    print(r.llen("list10")) # 0
    print(r.lrange("list10", 0, -1)) # []

    r.lpushx("list2", 77) # 这里"list2"之前已经存在，忘列表最左边添加一个元素，一次只能添加一个
    print(r.llen("list10")) # 列表长度
    print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素)
    """
    4-往已经有的name的列表的右边添加元素，没有的话无法创建
    """
    r.rpushx("list2", 99) # 这里"list2"之前已经存在，往列表的最右边添加一个元素，一次只能添加一个
    print(r.llen("list2")) # 列表长度
    print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0到-1(最后一个元素)
    """
    5-新增(固定索引号位置插入元素)
    linsert(name, where, refvalue, value)
    在name对应的列表的某一个值前或后插入一个新值
    name-redis的name
    where,before或after
    refvalue,标杆值,即：在它前后插入数据
    value,要插入的数据
    """
    r.linsert("list2", "before", "55", "00")
    print(r.lrange("list2", 0, -1)) # 切片取出值，范围是索引号0-最后一个元素
    """
    6-修改(指定索引号进行修改)
    r.lset(name, index, value)
    对name对应的list中的某一个索引位置重新赋值
    参数:
    name-redis的name
    index-index的索引位置
    value-要设置的值
    """
    r.lset("list2", 0, -11) # 把索引号是0的元素修改成-11
    print(r.lrange("list2", 0, -1))
    """
    7-删除(指定值进行删除)
    def lrem(self, name, count, value)
    在name对应的list中删除指定的值
    参数:
    name-redis的name
    count, count = 0 删除列表中所有的特定值
    count > 0 从前往后面删除 假如count = 2 ，则从前往后面删2个
    count < 0 从后往前面删除 假如count = 2 , 则从后往前面删2个
    value-要删除的值
    """
    print("--------------------------")
    r.lrem("list2", 1, "-11") # 将列表中左边第一次出现的"-11"删除
    print(r.lrange("list2", 0, -1))
    r.lrem("list2", -1, "99") # 将列表中右边第一次出现的"99"删除
    print(r.lrange("list2", 0, -1))
    r.lrem("list2", 0, "66") # 将列表中所有的"66"删除
    print(r.lrange("list2", 0, -1))
    """
    8-删除并返回
    lpop(name),lrem(name)
    在name对于的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
    rpop(name)表示从右向左操作
    """
    r.lpop("list2") # 删除列表最左边的元素，并且返回删除的元素
    print(r.lrange("list2", 0, -1))
    r.rpop("list2") # 删除列表最右边的元素，并且返回删除的元素
    print(r.lrange("list2", 0, -1))
    """
    9-删除索引之外的值
    ltrim(name, start, end)
    在name对于的列表中移除没有在start-end索引之间的值
    参数；
    name,redis的name
    start,索引的起始位置
    end,索引结束位置
    """
    r.ltrim("list2", 0, 1) # 删除索引号是0-1之外的元素，只保留索引号是0-2的元素
    print(r.lrange("list2", 0, -1))
    """
    10-取值(根据索引号取值)
    lindex(name, index)
    在name对应的列表中根据索引获取列表元素
    """
    print(r.lindex("list2", 0)) # 取出索引号是0的值
    """
    11-移动 元素从一个列表移动到另外一个列表
    rpoplpush(src, dst)
    从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
    参数:
    src,要取数据的列表的name
    dst,要添加数据的列表的name
    """
    print(r.lrange("list1", 0, -1))
    r.rpoplpush("list1", "list2")
    print(r.lrange("list2", 0, -1))
    """
    12-移动 元素从一个列表移动到另外一个列表 可以设置超时
    brpoplpush(src, dst, timeout=0)
    从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
    参数:
    src,取出并要移除元素的列表对应的name
    dst,要插入元素的列表对应的name
    timeout,当src对应的列表中没有数据时，
    阻塞等待其有数据的超时时间(秒)，0表示永远阻塞
    """
    # 有数据了马上移过去，没有就阻塞，超时时间到了还没有成功，就退出，不移了
    # 这个概念很新奇--1-19
    r.brpoplpush("list1", "list2", timeout=2)
    print(r.lrange("list2", 0, -1))
    """
    13-一次移除多个列表
    blpop(keys, timeout)
    将多个列表排列，按照从左到右去pop对应列表的元素
    参数:
    keys:redis的name集合
    timeout,超时时间；当元素所有列表的元素获取完之后，
    阻塞等待列表内有数据的时间(秒),0表示永远阻塞
    b.brpop(keys, timeout)同blpop,将多个列表排列，
    按照从右向左去移除各个列表内的元素
    """
    print("------------------")
    r.lpush("list20", 3, 4, 5)
    r.lpush("list21", 3, 4, 5)
    print(r.lrange("list20", 0, -1))
    while True: # 这是个无限循环 the one ring!
        r.blpop(["list20", "list21"], timeout=2) # 20里面的东西 弹出去放到21里面去 有意思！
        print(r.lrange("list20", 0, -1), r.lrange("list21", 0, -1))
    pass


def set_test():
    """
    操作set
    1-新增
    sadd(name, values)
    name-对应的集合中添加元素
    :return:
    """
    r.sadd("set1", 33, 44, 55, 66) # 在集合中添加元素
    """
    2-获取元素个数 类似于len
    scard(name)
    获取name对应的集合中元素个数
    """
    print(r.scard("set1"))
    """
    3-获取集合中所有的成员
    smembetrs(name)
    获取name对应的集合的所有成员
    """
    print(r.smembers("set1")) # 获取集合中所有的成员
    # 获取集合中所有的成员--另外一种方式
    print(r.sscan('set1'))
    """
    获取集合中所有的成员--迭代器方式
    sscan_iter(name, match=None, count=None)
    同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大
    """
    for i in r.sscan_iter("set1"):
        print(i)
    """
    4-差集，第一个name对应的集合中去除相同的取不同的
    【以第一个name为主去除相同取不同】
    sdiff(keys, *args)
    在第一个name对应的集合中且不在其他name对应的集合的元素集合
    去除相同的取不同的
    """
    r.sadd("set2", 11, 22, 33)
    print(r.smembers("set1")) # 获取集合中所有的成员
    print(r.smembers("set2"))
    print(r.sdiff("set1", "set2")) # 在集合set1但是不在集合set2中
    print(r.sdiff("set2", "set1")) # 在集合set2但是不在集合set1中
    """
    差集--差集存在一个新的结合中
    sdiffstore(dest, keys, *args)
    获取第一个name对应的集合中且不在其他name对应的集合，
    在将其新加入到dest对应的集合中
    """
    # 在集合set1但是不在集合set2中,把结果放到了set3里面
    r.sdiffstore("set3", "set1", "set2")
    print(r.smembers("set3"))
    """
    5-交集，第一个name对应的集合中取相同的
    sinter(keys, *args)
    获取name对应集合的交集
    """
    print(r.sinter("set1", "set2")) # 取两个集合的交集-33
    """
    交集--交集存在一个新的集合中
    sinterstore(dest, keys, *args)
    获取多一个name对应集合的并集，再将其加入到dest对应的集合中
    """
    print(r.sinterstore("set3", "set1", "set2")) # 取2个集合的交集
    print(r.smembers("set3"))
    """
    6-并集 合并不同的----这挺方便
    sunion(keys, *args)
    获取多个name对应的集合的并集
    """
    print(r.sunion("set1", "set2"))
    """
    并集--并集存在一个新的集合
    sunionstore(dest, keys, *args)
    获取一个name对应的集合的并集，并将结果保存到dest对应的集合中
    """
    # 如果打印，是打印的移过去的6个！！！
    r.sunionstore("set3", "set1", "set2")
    print(r.smembers('set3'))
    """
    7-判断是否是集合的成员，类似in
    sismember(name, value)
    检查value是否是name对应的集合的成员，结果为True和False
    """
    print(r.sismember("set1", 33)) # 33是集合的成员
    print(r.sismember("set1", 23)) # 23不是集合的成员
    """
    8-移动
    smove(str, dst, value)
    将某个成员从一个集合移动到另外一个集合
    """
    r.smove("set1", "set2", 44)
    print(r.smembers("set1"))
    print(r.smembers("set2"))
    """
    9-删除--随机删除并且返回被删除值(这难道是为了避免缓存雪崩?)
    spop(name)
    从集合移除一个成员，并将其返回，
    说明一下，集合是无序的，所以是随机删除的
    """
    print(r.spop("set2")) # 这个删除的值是随机删除的，集合是无序的
    print(r.smembers("set2"))
    """
    10-删除--指定值删除
    srem(name, values)
    在name对应的集合中删除某些值
    """
    print(r.srem("set2", 11)) # 从集合中删除指定值11
    print(r.smembers("set2"))
    pass


def sorted_set_test():
    """
    set操作，set集合就是不允许重复的列表，本身是无序的
    有序集合，在集合的基础上，为每元素排序
    元素的排序需要根据另外一个值来进行比较
    所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序
    :return:
    """
    """
    操作sorted set
    1-新增
    def zadd(
        self, name, mapping, nx=False, xx=False, ch=False, incr=False, gt=None, lt=None
    ):
    在name对于的有序集合中添加元素
    更改写法为：connect.zadd('key',{'value1':'score1','value2':'scote2',.....})
    """
    r.zadd("zset1", {"n1":11, "n2":22})
    r.zadd("zset2", {"m1":22, "m2":44})
    """
    2-获取有序集合元素个数 类似于len
    zcard(name)
    获取name对于的有序集合元素的数量
    """
    print(r.zcard("zset1")) # 集合长度
    """
    3-获取有序集合的所有元素
        def zrange(
        self,
        name,
        start,
        end,
        desc=False,
        withscores=False,
        score_cast_func=float,
        byscore=False,
        bylex=False,
        offset=None,
        num=None,
    ):
    按照索引范围获取name对于的有序集合的元素
    参数:
    name-redis的name
    start,有序集合索引起始位置(非分数)
    end,有序集合索引结束位置(非分数)
    desc,排序规则，默认按照分数从小到大排序
    withscores,是否获取元素的分数，默认只获取元素的值
    socre_caset_func,对分数进行数据转换的函数
    """
    print(r.zrange("zset1", 0, -1)) # 获取有序集合中所有元素
    print(r.zrange("zset2", 0, -1, withscores=True)) # 获取有序集合中所有元素和分数
    """
    3-1 从大到小排序(同zrange,集合是从大到小排序的)
    def zrevrange(self, name, start, end, withscores=False, score_cast_func=float)
    """
    print(r.zrevrange("zset1", 0, -1)) # 只获取元素，不显示分数
    print(r.zrevrange("zset1", 0, -1, withscores=True)) # 获取有序集合中所有元素和分数，分数倒序
    """
    3-2 按照分数范围获取name对应的有序集合的元素
    def zrangebyscore(
        self,
        name,
        min,
        max,
        start=None,
        num=None,
        withscores=False,
        score_cast_func=float,
    )
    """
    for i in range(1, 30):
        element = 'n' + str(i)
        r.zadd("zset3", {element:i})
    print(r.zrangebyscore("zset3", 15, 25)) # 在分数是15-25之间，取出符合条件的元素
    print(r.zrangebyscore("zset3", 12, 22, withscores=True)) # 在分数是12-22之间，取出符合条件的元素(带分数)
    """
    3-3 按照分数范围获取有序集合的元素并排序(默认从大到小排序)
    def zrevrangebyscore(
        self,
        name,
        max,
        min,
        start=None,
        num=None,
        withscores=False,
        score_cast_func=float,
    )
    """
    # 在分数是22-11之间，取出符合条件的的元素，按照分数从小到大
    print(r.zrevrangebyscore("zset3", 22, 11, withscores=True))
    """
    3-4 获取所有元素--迭代器
    def zscan_iter(self, name, match=None, count=None, score_cast_func=float):
    """
    for i in r.zscan_iter("zet3"):
        print(i) # key和分数一起打印
    print(r.zscan("zset3")) # 这个也是获取所有
    """
    4-zcount(name, min, max)
    获取name对应的有序集合中 分数在[min,max]之间的个数
    """
    print(r.zrange("zset3", 0, -1, withscores=True))
    print(r.zcount("zset3", 11, 22)) # 分数在[min,max]之间的个数!!
    """
    5-自增
    def zincrby(self, name, amount, value):
    自增name对应的有序集合的name对应的分数
    """
    # 每次将n2的分数自增2 注意value相当于key
    r.zincrby("zset3", amount=2, value="n2") # 这里和视频不一样！！
    print(r.zrange("zset3", 0, -1, withscores=True))
    """
    6-获取值的索引号
    zrange(name,value)
    获取某个值在name对应的有序集合中的索引(从0开始)
    def zrevrank(self, name, value) 从大到小排序 返回键为name的zset中元素的倒数排名（按score从大到小排序），即名次
    """
    print(r.zrank("zset3", "n1"))
    print(r.zrank("zset3", "n5"))
    print(r.zrevrank("zset3", "n1"))
    """
    7-删除--指定值删除
    zrem(name, values)
    删除name对应的有序集合中值是values的成员
    """
    r.zrem("zset3", "n3") # 删除有序集合中的元素n3, 删除单个
    print(r.zrange("zset3", 0, -1))
    """
    8-删除--根据排序范围删除，按照索引号来删除
    def zremrangebyrank(self, name, min, max)
    根据排行范围删除
    """
    # 删除有序集合中索引号是0,1的元素
    r.zremrangebyrank("zset3", 0, 1)
    print(r.zrange("zset3", 0, -1))
    """
    9-删除--根据分数范围删除
    def zremrangebyscore(self, name, min, max):
    根据分数范围删除
    """
    r.zremrangebyscore("zset3", 11, 22) # 删除有序集合中分数是11-22的元素
    print(r.zrange("zset3", 0, -1))
    """
    10-获取值对应的分数
    def zscore(self, name, value):
    获取name对应有序集合中value的分数
    """
    print(r.zscore("zset3", "n27")) # 获取元素n27对应的分数27
    pass


def other_test():
    """
    其他操作
    :return:
    """
    """
    1-redis中以层级、目录形式存储数据
    """
    r.set('user:01', 'zhangsan')
    print(r.get('user:01'))
    """
    2-删除
    delete(*names)
    根据删除redis中的任意数据类型(string,hash,list,set,sorted set)
    """
    r.delete("user:01")
    """
    3-检查name是否存在
    exist(name)
    检测redis的name是否存在,存在就是True,False不存在
    """
    print(r.exists("zset1")) # 1
    print(r.exists("zset13")) # 0
    """
    4-模糊匹配
    keys(pattern='')
    根据模型获取redis的name
    更多
    keys * 匹配数据库中的所有key
    keys h?llo 匹配hello,hello和hxllo等
    keys hllo 匹配hllo和heeeeello等
    keys h[ae]llo匹配hello和hallo,但不匹配hillo
    功能：比如匹配某一批key然后全部删掉(可for循环delete)
    """
    print(r.keys("zset*"))
    """
    5-设置超时时间
    expire(name, time)
    为某个redis的某个name设置超时时间
    """
    # lpush本身没有设置过期时间选项，但可以通过这种方式实现
    r.lpush("list5", 11, 22)
    r.expire("list5", time=10) # 10秒
    print(r.lrange("list5", 0, -1))
    print(r.lrange("list5", 0, -1))
    """
    6-重命名
    rename(src, dst)
    对redis的name重命名
    """
    print(r.lpush("list5", 11, 22))
    r.rename("list5", "list5-1")
    print(r.lrange("list5", 0, -1))
    print(r.lrange("list5-1", 0, -1))
    """
    7-随机获取name
    randomkey()
    随机获取一个redis的name(不删除)
    """
    print(r.randomkey())
    """
    8-获取类型
    type(name)
    获取name对应值的类型
    """
    print(r.type("list5-1"))
    """
    9-查看所有元素
    scan()
    """
    print(r.hscan("hash2")) # hash
    print(r.sscan("set3")) # set
    print(r.zscan("zset2")) # zset
    print(r.getrange("string1", 0, -1)) # string
    print(r.lrange("list5-1", 0, -1)) # list
    print(r.smembers("set3")) # set
    print(r.zrange("zset3", 0, -1))
    print(r.hgetall("hash1")) # hash
    """
    10-查看所有元素--迭代器
    """
    for i in r.hscan_iter("hash1"):
        print(i)
    for i in r.sscan_iter("set3"):
        print(i)
    for i in r.zscan_iter("zset3"):
        print(i)
    # 11-当前redis包含多少个key，返回个数
    print(r.dbsize())
    # 12-查询所有的key，返回具体的key
    print(r.keys())
    # 13-清空redis中的所有数据
    r.flushdb() # 干净，谨慎使用





    pass


def tmp_test():
    # string_test() 1
    # hash_test 2
    # list_test() 3
    # set_test() 4
    # sorted_set_test() 5
    # r.zincrby("zset3", amount=2, value="n2")  # 这里和视频不一样！！
    # print(r.zrange("zset3", 0, -1, withscores=True))
    other_test()
    pass


if __name__ == "__main__":
    tmp_test()

"""
总结-api学习是大概过一遍,很枯燥
以后string里面的set,get最常用
hash里面的hset,hget,hmget,hgetall
list里面的lpush,lrange
set和sorted都用的比较少


"""