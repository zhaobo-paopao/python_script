import os
import sys

from pyspark import SparkConf, SparkContext

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
conf = SparkConf().setAppName("wordCountRDD").setMaster("local[*]")
sc = SparkContext(conf=conf)
# 输入文本
lines = sc.parallelize(["hello spark", "hello python", "spark spark"])
# 切单词
words = lines.flatMap(lambda lines: lines.split(" "))
# 变成word， 1
pairs = words.map(lambda word: (word, 1))
# 分组求和
word_count = pairs.reduceByKey(lambda a, b: a + b)
# 打印结果
print(word_count.collect())
sc.stop()
