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
"""
--这个需要时刻记住
新增数据
insert into 表名(列名1,列名2,...) values(对应列的值1,对应列的值2,...)
插入单条数据
insert into tb1(name,password) values('武沛齐',"123123");
插入多条数据
insert into tb1(name,password) values('武沛齐','123123'),('alex','123');
省去列名--默认情况下按从左到右插[基本不用--看起来不规范]
insert into tb1 values('武沛齐','123123'),('alex','123')

删除数据
delete from 表名
delete from 表名 where 条件
delete from tb1;
delete from tb1 where id >9;

修改数据
update 表名 set 列名=值;
update 表名 set 列名=值 where 条件;

update tb1 set name="wupeiqi"; #把所有name都改为wupeiqi
update tb1 set name="wupeiqi" where id=1;#更改某一列
update tb1 set age=age+1;# age需要是整形利用原来的值+
# concat可以拼接字符串
update users set name=concat(name,"123") whete id=2;

查询数据库
select * from 表名
select 列名1,列名2,列名3 from 表名
select 列名,列名 as 别名,列名 from 表名
select * from 表名 where 条件

select * from tb1;
select id,name,age from tb1;
select id,name as N,age, from tb1
# 额外再加一个111列
select id,name as N,age,111 from tb1

select * from tb1 where id = 1
select * from tb1 where id > 1
select * from tb1 where id != 1
seletc * from tb1 where name="wupeiqi" and password="123"
"""
