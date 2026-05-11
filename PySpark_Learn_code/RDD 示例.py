# Python
from pyspark import SparkContext
import os,sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# 创建SparkContext
sc = SparkContext("local", "RDD Example")

# 创建RDD
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)  # 从列表创建RDD

# Transformation操作 (惰性)
rdd_squared = rdd.map(lambda x: x * x)  # 每个元素平方
rdd_filtered = rdd.filter(lambda x: x > 2)  # 过滤大于2的元素

# Action操作 (触发计算)
print("原始RDD:", rdd.collect())  # [1, 2, 3, 4, 5]
print("平方RDD:", rdd_squared.collect())  # [1, 4, 9, 16, 25]
print("过滤RDD:", rdd_filtered.collect())  # [3, 4, 5]
print("总和:", rdd.reduce(lambda a, b: a + b))  # 15

# 关闭SparkContext
sc.stop()