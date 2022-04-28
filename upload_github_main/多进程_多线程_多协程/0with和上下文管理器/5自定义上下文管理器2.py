from contextlib import contextmanager
# https://www.bilibili.com/video/BV1qT4y1Y76U?p=2
@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    # 有yield的是生成器
    yield f
    f.close()

with my_open('1.txt', 'w') as f:
    f.write("111111111")

"""
总结：
之所以用上下文管理器，是因为在开发中一般都会用到系统资源
比如文件，网络，设备，此时我们在使用完毕之后一定要关闭
一般使用f.close()这种方式容易产生异常，导致f.close()不会被调用
导致系统资源一直没有被释放
我们这时推出了with这种简单的方式来规避这个问题
所以需要学习上下文管理器

上下文管理器简单分两部分
一部分是申请资源，另一部分是释放资源
with中使用资源,with会自动申请资源以及释放资源
这种方式更不容易出错

"""

