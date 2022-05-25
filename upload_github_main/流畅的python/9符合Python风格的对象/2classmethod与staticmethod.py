class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statemeth(*args):
        return args

print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
print(Demo.statemeth())
print(Demo.statemeth('spam'))