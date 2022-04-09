"""
提要：
以金庸笑傲江湖为历史背景来练练面向对象
令狐冲自小无父无母，由师父华山派掌门“君子剑”岳不群和其妻师母宁中则扶养授武，情同亲生父母。
知识点：
类属性【变量】,实例属性【变量】,私有属性【变量】,私有方法,新式类
私有属性和私有方法属于封装这个特性
"""
class People(object):
    # 类属性
    occupation = '练武之人'
    def __init__(self,name,age,sex,nickname,__skill_number_1):
        # 实例属性
        self.name = name
        self.age = age
        self.sex = sex
        self.nickname = nickname
        # 内功--私有属性
        self.__skill_number_1 = __skill_number_1

    def get_skill_number_1(self):
        print('%s拥有的内功名称是%s'%(self.name,self.__skill_number_1))
        # 私有方法一般是不允许外部直接调用的
        self.__exercise()

    def modification_skill_number_1(self,skill_name):
        self.__skill_number_1 = skill_name

    def __exercise(self):
        print('%s今天修炼了%s'%(self.name,self.__skill_number_1))

Ling = People('令狐冲',26,'男','无绰号','吸星大法')
Yue = People('岳不群',37,'男','君子剑','紫霞神功')
Ning = People('宁中则',35,'女','华山玉女','无名称内功')
# 调用类属性
print(People.occupation)
print(Ling.occupation)
# 修改类属性
People.occupation = '江湖上行走的人'
print(People.occupation)
# 调用实例属性
print(Ling.nickname)
print(Yue.nickname)
# 修改实例属性
Ling.nickname = '令狐公子'
print(Ling.nickname)
print('--------------------------------------------------------------------------------')
# 调用私有属性
Ling.get_skill_number_1()
# 修改私有属性
Ling.modification_skill_number_1('加强版吸星大法')
Ling.get_skill_number_1()
# 实例类.类名_变量名--不推荐使用的直接访问私有属性
print(Yue._People__skill_number_1)
Yue._People__skill_number_1 = '修改后的紫霞神功'
Yue.get_skill_number_1()
print('--------------------------------------------------------------------------------')
# 实例名._类名+方法名()--外部调用私有方法--一般不这么用
Yue._People__exercise()





