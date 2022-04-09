"""
校园管理系统
设计一个培训机构管理系统，有总部、分校，有学员、老师、员工，实现具体如下需求：
1. 有多个课程，课程要有定价
2. 有多个班级，班级跟课程有关联
3. 有多个学生，学生报名班级，交这个班级对应的课程的费用
4. 有多个老师，可以分布在不同校区，上不同班级的课
5. 有多个员工，可以分布在不同校区在总部可以统计各校区的账户余额、员工人数、学员人数
6. 学生可以转校、退学
"""
import time    #导入时间模块
#定义个学校
class School:
    #初始化
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.branches = {}           #统计分校的信息
        self.staff_lst = []        #员工总数存在列表里
        self.class_list = []        #学员列表
        self.__money_account = 0     #初始的费用为0，后面进行计费

    #发工资
    def pay_roll(self):
        print("给大家发工资了")

    #统计员工人数
    def count_staff_num(self):
        """统计公司各分校员工人数"""
        total_staff_num = len(self.staff_lst)       #员工列表的长度用来计算总校总员工数
        for i in self.branches:                     #遍历分校，分别计算
            total_staff_num += self.branches[i].count_staff_num()  # 统计分校人数
        print("[%s]总员工数量:%s" % (self.name, total_staff_num))
        return total_staff_num

    def count_student_num(self):
        """统计学员总数人数"""
        total_student_num = 0
        for i in self.class_list:       #遍历学员列表
            total_student_num += len(i.stu_lst)  # 统计分校人数
        print("[%s]总学员数量:%s" % (self.name, total_student_num))


    #新员工注册
    def new_staff_enrollment(self,staff_obj):
        self.staff_lst.append(staff_obj)    #将员工加入列表

        # 统计学员人数




    # 统计总的费用
    def count_account(self):
        balance = self.__money_account
        for i,v in  self.branches.items():
            balance += v.__money_account
        print(f"总钱数:{balance}")


    #收钱方法
    def collect_fee(self,amount,name_obj,cause):
        self.__money_account += amount
        # print(f"{time.strptime('%Y-%m-%d %H:%M:%S')}{self.name}校区收到{name_obj}转账{amount}元，转账原因{cause}")
        print("%s,校区[%s]收到[%s]转账[%s],交费原因[%s]..." % (time.strftime("%Y-%m-%d %H:%M:%S"),
                                                     self.name, name_obj.name, amount, cause))
# ===================================================================================================
#定义分校
class BranchSchool(School):
    def __init__(self, name, addr, headquater_obj):
        super().__init__(name, addr)
        self.headquater_obj = headquater_obj  # 总部的对象
        self.headquater_obj.branches[name] = self  # 把自己添加到总部的分校列表
# ================================================================================================================
#定义员工
class Staff:
    def __init__(self,name,age,position,salary,dept,school_obj):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.dept = dept
        self.school_obj = school_obj
        school_obj.new_staff_enrollment(self)
# =======================================================================================================================
#定义班级
class Class:
    def __init__(self,course_obj,school_obj,class_num,headquater_obj):
        self.class_num = class_num
        self.course_obj = course_obj
        self.school_obj = school_obj
        self.stu_lst = []  # 学员列表     #学员在这个班级的列表
        self.headquater_obj = headquater_obj
        self.headquater_obj.class_list.append(self)

    def creat_teaching_record(self):
        pass

    def get_class_name(self):
        return f"{self.school_obj.name}-{self.course_obj.name}-{self.class_num}期"

    def drop_out(self,stu_obj):
        self.stu_lst.remove(stu_obj)
        print(f"学员{stu_obj.name}从{self.get_class_name()}退学了")

# ======================================================================================================================
#定义课程
class Course:
    def __init__(self,name,price,degree):
        self.name = name
        self.price = price
        self.degree = degree
# ========================================================================================================================
#定义讲师
class Teacher(Staff):

    def teaching(self,class_obj):
        pass
# =========================================================================================================================
#定义学员
class Student(object):
    def __init__(self,name,age,degree,class_obj,balance):
        self.name = name
        self.age = age
        self.degree = degree
        self.class_obj = class_obj     #报名班级的对象
        self.balance = balance
        self.class_obj.stu_lst.append(self) #学生找到自己的班级，将自己加上

    def pay_tuition(self):          #交学费的方法
        self.balance -= self.class_obj.course_obj.price
        # self.class_obj.school.obj.collect_fee(self.class_obj.course_obj.price,self,f"交{self.class_obj.get_class_name()}学费")

        self.class_obj.school_obj.collect_fee(self.class_obj.course_obj.price, self,
                                                "交%s学费" % self.class_obj.get_class_name())
    #转校方法
    def transfer(self, new_class_obj):
        """转学"""
        self.class_obj.stu_lst.remove(self)
        self.class_obj = new_class_obj
        self.class_obj.stu_lst.append(self)
        print(f"{self.name}转入{self.class_obj.school_obj.name}的{self.class_obj.course_obj.name}")



    def __repr__(self):
        return "学生:%s,班级:%s" % (self.name, self.class_obj.get_class_name())


headquater = School("北京总校区","沙河")
bj1 = BranchSchool("北京分校","汇德商厦401",headquater)
sh1 = BranchSchool("上海1分校","上海1区",headquater)
sh2 = BranchSchool("上海2分校","上海2区",headquater)
sz1 = BranchSchool("深圳分校","深圳1区",headquater)

#员工实例化
staff1 = Staff("Alex",26,"CEO",60000,"总经办",headquater)
staff2 = Staff("周小月",23,"HR",6000,"HR",headquater)
t1 = Teacher("Mjj",27,"前端开发讲师",30000,"教研部",bj1)
t2 = Teacher("银角大王",27,"Python讲师",45000,"教研部",sz1)
t3 = Teacher("苑日天",23,"Java讲师",40000,"教研部",sh1)


# 初始化课程
py_course = Course("Python开发",21800,"本科")
linux_course = Course("Linux云计算运维",19800,"专科")
go_course = Course("GO开发",9800,"本科")


# 初始化班级
class1 = Class(py_course,bj1,21,headquater)
class2 = Class(linux_course,sz1,4,headquater)
class3 = Class(go_course,sh1,11,headquater)

# 初始化学员
stu1 = Student("blackgirl",22,"本科",class1,30000)
stu2 = Student("李晓虎",23,"专科",class2,25000)
stu3 = Student("林爱根",26,"本科",class3,13000)
stu4 = Student("刘清蒸",21,"本科",class3,10000)
stu5 = Student("海底捞哥",21,"专科",class1,20000)

# for i in (stu1,stu2,stu3,stu4):
#     i.pay_tuition()


# print(class3.stu_lst)


# headquater.count_account()

headquater.count_staff_num()
# headquater.count_student_num()
#
# # 退学
# stu5.class_obj.drop_out(stu5)
#
# stu1.transfer(class3