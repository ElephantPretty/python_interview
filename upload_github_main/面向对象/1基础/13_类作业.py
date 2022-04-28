import time

class School(object):
    """总部"""
    def __init__(self,name,address,branch_schools):
        self.name = name
        self.address = address
        print('初始化校区[%s],地址:%s...'%(self.name,self.address))
        # 分校列表，默认为空
        self.branch_schools = []
        # 员工总数存在列表里面
        self.staff_lst = []
        # 学员列表
        self.class_list = []
        #初始费用为０，后面进行计费
        self.__money_account = 0


    def pay_roll(self):
        # 发工资
        print("给大家发工资了")

    def count_staff_num(self):
        # 统计员工人数
        print("[%s]总员工数量:%s"%(self.name,len(self.staff_lst)))

    def count_stu_num(self):
        # 统计学员人数
        pass

    def new_staff_enrollment(self,staff_obj):
        # 新员工注册
        self.staff_lst.append(staff_obj)
        print("校区[%s]的[%s]部门在[%s]入职一名新同事[%s],职位是[%s]"%(staff_obj.school_obj.name,
              staff_obj.dept, time.strftime('%Y-%m-%d',time.localtime(time.time())),staff_obj.name,staff_obj.position))

    # 收钱方法
    def collect_fee(self,amount,name_obj,cause):
        self.__money_account += amount
        print("%s,校区[%s]收到[%s]转账[%s],交费原因[%s]..." % (time.strftime("%Y-%m-%d %H:%M:%S"),
                                                     self.name, name_obj.name, amount, cause))

    # 统计总的费用
    def count_account(self):
        print("[%s]账户余额:%s"%(self.name,self.__money_account))

class BranchSchool(School):
    """分校"""
    def __init__(self,name,address,__school_obj):
        super().__init__(name,address,[])
        """
            三种构造函数的区别：
            当子类不做初始化的时候，会自动继承父类的属性；
            当子类做初始化（子类中包含新的属性）的时候，子类不会自动继承父类的属性；
            当子类做初始化（子类中包含新的属性）的时候，如果子类调用super初始化了父类的构造函数，那么子类会继承父类的属性。
        """
        # 所属上级校区对象
        self.__school_obj = __school_obj
        # 把自己添加到总部的分校列表
        self.branch_schools.append(self)

class Course(object):
    def __init__(self,name,price,degree):
        self.name = name
        # 学费
        self.price = price
        self.degree = degree


class Class(BranchSchool):
    def __init__(self,course_obj,school_obj,class_num,headquarter_obj):
        """

        :param course_obj: 课程对象
        :param school_obj: 所属校区【分校】
        :param class_num: 第几班 比如学前1班 学前2班
        :param headquarter_obj: 所属总校
        """
        self.course_obj = course_obj
        self.school_obj = school_obj
        self.class_num = class_num
        # 学员列表
        self.stu_lst = []
        self.headquarter_obj = headquarter_obj
        print("校区[%s]开设了[%s]课程第[%s]班，开班日期是[%s]"%(
        school_obj.name,course_obj.name,class_num,time.strftime('%Y-%m-%d', time.localtime(time.time()))
        ))

    def create_teaching_record(self):
        # 创建上课
        pass

    def drop_out(self,stu_obj):
        self.stu_lst.remove(stu_obj)
        print(f"学员{stu_obj.name}从{self.course_obj.name}退学了")

    def view(self):
        for i in self.stu_lst:
            print("[学生:%s,班级:%s]"%(i.name,i.class_obj.course_obj.name))

class Staff(object):
    def __init__(self,name,age,position,salary,dept,school_obj):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.dept = dept
        self.school_obj = school_obj
        # 新员工注册
        school_obj.new_staff_enrollment(self)

    def hehe(self):
        # 测试子类不同的构造方法是否会继承父类方法
        print("111")


class Teacher(Staff):
    # 当子类不做初始化的时候，会自动继承父类的属性；
    def teaching(self,class_obj):
        pass


class Student(Class):
    def __init__(self,name,age,degree,class_obj,balance):
        self.name = name
        self.age = age
        self.degree = degree
        # 在哪个班
        self.class_obj = class_obj
        self.balance = balance # 学生自己身上的钱
        # 学生找到自己班级，讲自己添加进去
        class_obj.stu_lst.append(self)

    def pay_tuition(self):  # 交学费的方法
        self.balance -= self.class_obj.course_obj.price
        print("学生支付了%s元"%(self.class_obj.course_obj.price))
        # 现在应当是系统缴费
        self.class_obj.school_obj.collect_fee(self.class_obj.course_obj.price,self,'课程报班费用')




wuhan_headquarters_school = School('武汉培训it蓝大象总部','武汉光谷广场地铁站C出口',[])
wuhan_branch_school_1 = BranchSchool('汉口分部001','青山区001',wuhan_headquarters_school)
wuhan_branch_school_2 = BranchSchool('汉口分部002','青山区002',wuhan_headquarters_school)
# 员工
staff1 = Staff('讲师1',25,'python讲师',150000,'政教室',wuhan_headquarters_school)
staff1 = Staff('讲师2',24,'java讲师',170000,'教研部',wuhan_branch_school_1)
tarcher1 = Teacher('教师1',24,'数据库教师',270000,'教研部',wuhan_branch_school_2)
tarcher2 = Teacher('教师2',24,'数据结构教师',370000,'教研部',wuhan_branch_school_2)
# 课程
course1 = Course('C开发',6000,'本科')
course2 = Course('python开发',3000,'本科')
# 班级
class1 = Class(course1,wuhan_branch_school_1,2,wuhan_headquarters_school)
class2 = Class(course2,wuhan_branch_school_2,1,wuhan_headquarters_school)
# 学员
stu1 = Student("大象001",22,"本科",class1,35000)
stu2 = Student("大象002",22,"本科",class1,20000)
stu3 = Student("大象003",22,"本科",class2,30000)
# 学员缴费
stu1.pay_tuition()
stu2.pay_tuition()
stu3.pay_tuition()
# 显示各个系列课程所包含的学生
class1.view()
class2.view()
# 统计校区余额
wuhan_headquarters_school.count_account()
wuhan_branch_school_1.count_account()
wuhan_branch_school_2.count_account()
# 统计员工数量
wuhan_headquarters_school.count_staff_num()
wuhan_branch_school_1.count_staff_num()
wuhan_branch_school_2.count_staff_num()
# 退学
class1.drop_out(stu1)
