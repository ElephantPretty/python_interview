import multiprocessing

def task(arg):
    pass


def run():
    p = multiprocessing.Process(target=task,args=('xx',))
    p.start()

if __name__ == '__main__':
    run()