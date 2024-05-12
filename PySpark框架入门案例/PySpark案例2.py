import json

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("jason_file")
sc = SparkContext(conf=conf)

file_rdd = sc.textFile("/home/songtao/Documents/orders.txt")
processed_rdd = file_rdd.flatMap(lambda x: x.split('|')).map(lambda x: json.loads(x)).map(
    lambda x: (x['areaName'], int(x['money'])))

data_by_city_rdd = processed_rdd.reduceByKey(lambda a, b: a + b)

# TODO 对各个城市销售额数排名，从大到小
result_1 = data_by_city_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1).collect()
print("----------------------------------")
print("需求1：对各个城市销售额排名，从大到小：")
for data in result_1:
    print(f"{data[0]}:{data[1]}元")

# TODO 全部城市，有哪些商品类别在出售
proecssed_rdd_2 = file_rdd.flatMap(lambda x: x.split('|')).map(lambda x: json.loads(x)).map(
    lambda x: (x['areaName'], x['category'])).distinct()
result_2 = proecssed_rdd_2.reduceByKey(lambda a, b: a + "," + b)
print("----------------------------------")
print("需求2：全部城市有哪些商品类别在售卖：")

for data in result_2.collect():
    print(f"{data[0]}:{data[1]}")

# TODO 北京市有哪些商品类别在售卖
print("----------------------------------")
print("需求3：北京市有哪些商品类别在售卖：")
result_3 = result_2.filter(lambda x: x[0] == "北京").collect()[0][1]
print(result_3)
