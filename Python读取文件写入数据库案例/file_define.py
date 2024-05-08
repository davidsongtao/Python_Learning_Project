import json

from Python面向对象FileReader案例.data_define import Data


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
