from file_define import FileReader, TextFileReader, JSONFileReader

text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
json_file_reader = JSONFileReader("D:/2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_file()  # 一月数据
feb_data = json_file_reader.read_file()  # 二月数据

all_data = jan_data + feb_data

"""
实现将读取到的数据all_data插入数据库
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
# 获取游标对象cursor()
cur = connection.cursor()

# 选择数据库
connection.select_db("orders")
# 使用游标对象，执行SQL语句

for data in all_data:
    sql = f"insert into order_info(date, order_id, money, province) values ('{data.date}','{data.order_id}',{data.money},'{data.province}');"
    cur.execute(sql)

# 关闭链接
cur.close()
