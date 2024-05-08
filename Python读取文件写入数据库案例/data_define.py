"""
需求分析:
    - 读取text文件和json文件的内容
    - 将取出的数据写入数据库
    - 运用面向对象编程
"""
class Data:
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"