"""
读取文件转换成RDD并完成：
    - 打印输出：热门搜索时间段（小时精度）Top3
    - 打印输出：热门搜索词Top3
    - 打印输出：统计黑马程序员关键字在哪个时段被搜索最多
    - 将数据转换为JSON格式，写出为文件
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("search_log_analysis")
conf.set("spark.default.parallelism", 1)
sc = SparkContext(conf=conf)

# 读取文件，将数据转换成RDD
rdd_file = sc.textFile("/home/songtao/Documents/search_log.txt")
rdd_process = rdd_file.map(lambda x: x.split("\t"))

# 打印输出：热门搜索时间段
# 构建二元元组，将时间里面的时与1组成一个二元元组
result_1 = rdd_process. \
    map(lambda x: (x[0].split(":")[0], 1)). \
    reduceByKey(lambda x, y: x + y). \
    reduce(lambda x, y: x if x[1] > y[1] else y)
print(f"热门搜索时间段是：{result_1[0]}点。")

# 需求2： 打印输出：热门搜索词TOP3
# 构建二元元组，将搜索词单独取出，与1组成二元元组，进行聚合相加
rdd_hot_word = rdd_process. \
    map(lambda x: (x[2], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
result_2 = rdd_hot_word[0][0] + "," + rdd_hot_word[1][0] + "," + rdd_hot_word[2][0]
print(f"热门搜索词TOP3是：{result_2}")

# 需求3： 打印输出：统计“黑马程序员”关键字在哪个时段被搜索最多
result_3 = rdd_process. \
    filter(lambda x: x[2] == "黑马程序员"). \
    map(lambda x: (x[0].split(":")[0], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(1)
print(f"'黑马程序员'关键字在{result_3[0][0]}点时段被搜索次数最多。")

# 需求4： 将数据转换为JSON格式，写出文件
# 4.1 转换为JSON格式的RDD
# 4.2 写出为文件
rdd_process.\
    map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank_1": x[3], "rank_2": x[4], "url": x[5]}). \
    saveAsTextFile("/home/songtao/Documents/output_json")
