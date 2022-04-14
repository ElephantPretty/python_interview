import pymysql

def register():
    print("用户注册")
    user = input("请输入用户名:")# alex
    password = input("请输入密码:")# sb
    # 连接指定数据
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                           passwd='123456',charset='utf8',
                           db='1pymysql')
    cursor = conn.cursor()
    # 执行sql语句（有sql注入风险，稍后讲解）
    sql = "insert into users(name,password) values('{}','{}')".format(user,password)
    cursor.execute(sql)
    conn.commit()
    # 关闭数据库连接
    cursor.close()
    conn.close()
    print("注册成功,用户名:{},密码:{}".format(user,password))


def login():
    print("用户登录")
    user = input("请输入用户名:")
    password = input("请输入密码:")
    # 连接指定数据
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',
                           passwd='123456',charset='utf8',
                           db='1pymysql')
    cursor = conn.cursor()
    # 执行sql语句
    sql = "select * from users where name='{}' and password='{}'".format(user,password)
    cursor.execute(sql)
    conn.close()
    """
    fetchall:获取所有数据，元组，没有则为None
    fetchone:获取第一条数据
    """
    result = cursor.fetchone()
    if result:
        print("登录成功",result)
    else:
        print("登陆失败")


# 新增 删除 修改 需要commit
def run():
    choice = input("1.注册;2.登录")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        print("输入错误")

if __name__ == "__main__":
    run()
