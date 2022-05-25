from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self,money):
        print("支付宝支付%d元."%money)


class Wechatpay(Payment):
    def pay(self,money):
        print("微信支付%d元."%money)


p1 = Wechatpay()
p2 = Alipay()
p1.pay(1)
p2.pay(10)
