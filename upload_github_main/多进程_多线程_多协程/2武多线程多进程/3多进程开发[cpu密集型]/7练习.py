from concurrent.futures import ProcessPoolExecutor


def task(filename):
    return {"total":filename}

def ourter(info, file_name):
    def done(res, *args, **kwargs):
        info["file_name"] = res.result()
    return done


def run():
    # 根据目录读取文件并初始化文件
    """
    :return:
    """
    info = {}
    pool = ProcessPoolExecutor(3)
    for i in range(3):
        fur = pool.submit(task,i)
        """
        因为是主进程调用，所以不担心进程之间资源共享的问题
        """
        fur.add_done_callback(ourter(info,i))
    pool.shutdown(True)
    print(info)


if __name__ == '__main__':
    run()

