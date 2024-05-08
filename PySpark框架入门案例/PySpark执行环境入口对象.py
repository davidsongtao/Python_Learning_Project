"""
演示获取PySpark的执行环境入口对象：SparkContext
并通过SparkContext对象获取当前PySpark的版本
"""
# 导包
from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/Python/python.exe"
# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 准备一个简单的rdd对象
rdd = sc.parallelize([1, 2, 3, 4, 5])


# 基于rdd对象调用.map()运算，把数值都乘10，返回运算结果
def fun(data):
    return data * 10


rdd2 = rdd.map(fun)

# 打印rdd2
print(rdd.collect())

# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()
