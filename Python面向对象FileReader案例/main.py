from prettytable.colortable import Themes
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts

from file_define import FileReader, TextFileReader, JSONFileReader
from data_define import Data
from pyecharts.charts import Bar
from pyecharts import options as opts

text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
json_file_reader = JSONFileReader("D:/2011年2月销售数据JSON.txt")

jan_data = text_file_reader.read_file()  # 一月数据
feb_data = json_file_reader.read_file()  # 二月数据

all_data = jan_data + feb_data

temp_dict = {}

for data in all_data:
    if data.date in temp_dict.keys():
        temp_dict[data.date] = temp_dict[data.date] + data.money
    else:
        temp_dict[data.date] = data.money

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(temp_dict.keys()))
bar.add_yaxis("销售额", list(temp_dict.values()), label_opts=opts.LabelOpts(is_show=False))
bar.set_global_opts(title_opts=opts.TitleOpts(title="销售额数据"))
bar.render()