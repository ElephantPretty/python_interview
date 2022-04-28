import json
import math

import flask
from concurrent.futures import ProcessPoolExecutor


app = flask.Flask(__name__)


def is_prime(n):
    """
    判断是否是素数
    :param n:
    :return:
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    # CPU密集型--用计算来模拟
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


# 定义时所依赖的函数必须已经声明完了
if __name__ == "__main__":
    """
    多线程非常自由，可共享公共区域，加锁就可以
    但是多进程【比如进程池】在flask中使用必须在app.run()之前使用
    且引用的函数此前必须声明完成
    """
    process_pool = ProcessPoolExecutor()
    app.run()


