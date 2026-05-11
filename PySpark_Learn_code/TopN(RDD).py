# 第一步：必须先创建 SparkContext（sc），这是源头！
import os
import sys

from pyspark import SparkConf, SparkContext

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
# # 创建 Spark 配置
conf = SparkConf().setAppName("topN").setMaster("local[*]")
# 创建 sc 对象
sc = SparkContext(conf=conf)
# 创建 RDD（分布式数据集）
rdd = sc.parallelize([("A", 100), ("B", 200), ("C", 150), ("D", 300)])
# 取 Top2：按第二个字段倒序取前2
"""
takeOrdered(N)：排序后取前 N 个
key=lambda x: -x[1]
x[1] = 取元组的第二个值(100、200、150、300)
-x[1] = 倒序取元组的第二个值(300、200、100、0)
前面加 - = 倒序（从大到小）
"""
topN = rdd.takeOrdered(2, key=lambda x: -x[1])
print(topN)
