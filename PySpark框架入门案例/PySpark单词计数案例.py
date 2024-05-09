"""
PySpark单词计数统计
    - 构建执行环境入口
    - 读取数据文件
    - 取出全部单词
    - 将所有单词转换成二元元组，单词为key,value设置为1
    - 分组求和
    - 打印输出结果
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("word_count_test")
sc = SparkContext(conf=conf)

file = open("/home/songtao/Documents/hello.txt", "r", encoding="UTF-8")

data_list = []

for line in file.readlines():
    line_update = line.strip().split(" ")
    for word in line_update:
        data_list.append(word)

rdd = sc.parallelize(data_list)
tuple_rdd = rdd.map(lambda x: (x, 1))  # 构建二元元组，单词为key,value设置为1

result = tuple_rdd.reduceByKey(lambda x, y: x + y)  # 通过key对value进行聚合相加计算

count_python = result.collect()[0][1]  # "python"出现的次数
count_pyspark = result.collect()[1][1]
count_itheima = result.collect()[2][1]
count_spark = result.collect()[3][1]
count_itcast = result.collect()[4][1]

print(
    f"'python'单词在文件中出现的次数为：{count_python}次。\n'pyspark'单词在文件中出现的次数为:{count_pyspark}次。\n'itheima'单词在文件中出现的次数为:{count_itheima}次。\n'spark'单词在文件中出现的次数为:{count_spark}次。\n'itcast'单词在文件中出现的次数为:{count_itcast}次。")
