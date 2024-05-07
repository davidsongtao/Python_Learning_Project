"""
使用面相对象开发text文件和json文件读取功能。实现读取文件内容返回一个list，list中存放数据对象。
    - zheg定义data_define类，用来定义数据相关的内容
    - 定义file_de关的内容：fine类，用来定义文件相关的内容
该文件用来定义文件相
    - 父类，定义FileReader的规范
    - 子类TextFileReader，继承父类，覆写read_file（）功能，实现读取text文件内容，返回list[Data]
    - 子类JsonFileReader,继承父类，覆写read_file（）功能，实现读取JSON文件内容，返回list[Data]
"""
import json

from data_define import Data


class FileReader:

    def read_file(self) -> list[Data]:
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_file(self) -> list[Data]:
        data_list: list[Data] = []
        # 成员方法，用来实现读取text文件内容，每条内容转换成一个Data对象，存入data_list中
        file = open(self.path, "r", encoding="UTF-8")
        temp_list = file.readlines()
        for line in temp_list:
            data = Data(line.strip().split(",")[0], line.strip().split(",")[1], int(line.strip().split(",")[2]),
                        line.strip().split(",")[3])
            data_list.append(data)
        file.close()
        return data_list


class JSONFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_file(self) -> list[Data]:
        data_list = []
        # 成员方法，用来实现读取json文件，每条内容转化成一个Data对象，存入data_list中
        file = open(self.path, "r", encoding="UTF-8")
        for line in file.readlines():
            json_data = json.loads(line)
            data = Data(json_data["date"], json_data["order_id"], int(json_data["money"]), json_data["province"])
            data_list.append(data)
        return data_list
