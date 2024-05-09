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

"""
使用textfile和flatmap进行取出
"""
rdd = sc.textFile("/home/songtao/Documents/hello.txt")
# 构建二元元组，单词为key,value设置为1 并 通过key对value进行聚合相加计算
result = rdd.flatMap(lambda x: x.split()).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)

count_python = result.collect()[0][1]  # "python"出现的次数
count_pyspark = result.collect()[1][1]
count_itheima = result.collect()[2][1]
count_spark = result.collect()[3][1]
count_itcast = result.collect()[4][1]

print(
    f"'python'出现的次数为：{count_python}次。\n'pyspark'出现的次数为:{count_pyspark}次。\n'itheima'出现的次数为:{count_itheima}次。\n'spark'出现的次数为:{count_spark}次。\n'itcast'出现的次数为:{count_itcast}次。")
