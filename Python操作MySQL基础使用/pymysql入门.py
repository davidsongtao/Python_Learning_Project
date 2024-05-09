"""
演示pymysql库的基础操作
"""

from pymysql import Connection

# 构建到mysql数据库的链接
connection = Connection(
    host="localhost",  # 主机名/IP地址
    port=3306,  # 端口
    user="root",  # 账户
    password="Dst881009.",  # 密码
    autocommit=True  # 设置执行数据更改的SQL语句时，不需要connection.commit()进行确认
)

print(f"版本信息：{connection.get_server_info()}")

"""
要执行费查询类的SQL语句，需要遵循以下步骤：
    - 1. 获取游标对象cursor()
    - 2. 选择数据库
    - 3. 使用游标对象，执行SQL语句
"""

# 执行非查询性质SQL e.g. 创建数据库，创建表，删除表...
# cursor = connection.cursor()
# connection.select_db("test")
# cursor.execute("create table test_pymysql(id int);")

# 执行查询类的SQL语句，获取查询结果，结果是一个元祖
# cursor = connection.cursor()
# connection.select_db("world")
# cursor.execute("select * from city")
#
# result = cursor.fetchall()  # 通过fetchall()获取查询结果，封装到元祖内
#
# for data in result:  # for循环取出每一条结果数据
#     print(data)

"""
pymysql在执行数据插入或更改的操作时，默认是需要提交更改的，
    - 通过connection.commit()确认即可
    - 或在构建链接对象的时候设置 autocommit = True，则不需要确认提交
"""
# connection.commit()  # 如果执行插入数据或数据更改，需要执行commit()进行确认

# 关闭链接
connection.close()
