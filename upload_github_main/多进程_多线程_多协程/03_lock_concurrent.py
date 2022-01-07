import threading
import time

lock = threading.Lock()


class Account:
    # 构造函数
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    with lock:# 加锁，其他线程在我线程执行完之前，无法进入这个代码，必须要有锁才能执行
        if account.balance >= amount:
            time.sleep(0.1)# 一定会导致当前线程阻塞，发生切换，若没加，线程是不可控的切换
            print(threading.current_thread().name, "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name, "余额", account.balance)
        else:
            print(threading.current_thread().name, "取钱失败，余额不足")


if __name__ == "__main__":
    account = Account(1000)
    tb = threading.Thread(name="ta", target=draw, args=(account, 800))
    ta = threading.Thread(name="tb", target=draw, args=(account, 800))
    ta.start()
    tb.start()


