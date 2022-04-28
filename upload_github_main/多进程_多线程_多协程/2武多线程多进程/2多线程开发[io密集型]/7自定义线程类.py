import threading

class MyThread(threading.Thread):
    def run(self):
        print("执行此线程",self._args)
        print(threading.current_thread().getName())
        

t = MyThread(args=(100,))
t.start()