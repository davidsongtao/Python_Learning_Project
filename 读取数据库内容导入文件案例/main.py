"""
实现读取数据库内容，将数据导出到文件中
"""
from pymysql import Connection

conn = Connection(
    host="localhost",  # 主机名/IP地址
    port=3306,  # 端口
    user="root",  # 账户
    password="Dst881009.",  # 密码
    autocommit=True  # 设置执行数据更改的SQL语句时，不需要connection.commit()进行确认
)

cur = conn.cursor()
conn.select_db("orders")
cur.execute("select * from order_info")
data = cur.fetchall()
for data_line in data:
    with open("D:/simple_data.txt", "a") as file:
        insert_data = str(data_line) + "\n"
        file.write(insert_data)
