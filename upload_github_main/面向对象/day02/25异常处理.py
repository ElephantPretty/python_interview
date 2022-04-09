name = "alex"
d = [1,2,3]

class YotubeConnectionError(BaseException):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


while True:
    try:
        num1 = int(input("n1>:"))
        num2 = int(input("n2>:"))
        res = num1 + num2
        # print("result:",res,name)
        print("result:", res)
        #主动触发异常
        raise YotubeConnectionError("在中国无法翻墙")
        # open("filetest")
        # d[3]
    except (KeyboardInterrupt,EOFError) as e:
        # 强类型错误
        print(e)
    except YotubeConnectionError as e:
        print(e)
    except IndexError as e:
        print(111)
        print(e)
    except AttributeError as e:
        print(e)
    except NameError as e:
        print(e)
    except ValueError as err:
        print("输出的值不合法，必须是数字")
    except Exception as e:
        print("发生错误",e)
    else:
        print("没有发生异常走这里")
    finally:
        print("不管有没有发生异常，都走这里")


