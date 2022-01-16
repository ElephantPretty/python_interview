import pymysql

# 连接Mysql(底层是socket)
# python3中的pymysql连接mysql时charset参数填utf8而非HTML中的charset的参数utf-8
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root',password='123456',
                       charset="utf8"
                       )
# 基于游标再发送指令
cursor = conn.cursor()

"""
1-查看数据库
发送指令
"""
cursor.execute("show databases")
# 获取指令的结果
result = cursor.fetchall()
print(result)

"""
2-创建数据库(新增、删除、修改)--这类指令必须要commit,和查询不同
发送指令
create database elephant111 default charset utf8 collate utf8_general_ci;
"""
# cursor.execute("create database wu_day1 default charset utf8 collate utf8_general_ci")
# conn.commit()

"""
3-查看数据库
发送指令
"""
cursor.execute("show databases")
# 获取指令的结果
result = cursor.fetchall()
print(result)

"""
4-删除数据库
发送指令
"""
# cursor.execute("drop database wu_day1")
# conn.commit()

"""
查看数据库
发送指令
"""
cursor.execute("show databases")
# 获取指令的结果
result = cursor.fetchall()
print(result)

"""
5-进入数据库，查看表
发送指令
"""
cursor.execute("use mysql")
cursor.execute("show tables")
result = cursor.fetchall()
print(result)


# 关闭连接
cursor.close() # 先关闭游标 python带我起飞
conn.close()
