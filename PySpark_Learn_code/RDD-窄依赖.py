import os
import sys

from pyspark import SparkConf, SparkContext

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# 创建 Spark 上下文
conf = SparkConf().setAppName("NarrowDependency").setMaster("local")
sc = SparkContext(conf=conf)

# 创建基础 RDD
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = sc.parallelize(data, 3)  # 3个分区

# 窄依赖转换链：所有操作都可在同一节点内完成
# map -> filter -> map
# 每个元素乘以2
# 过滤大于5的元素
result = (
    rdd.map(lambda x: x * 2).filter(lambda x: x > 5).map(lambda x: x + 1)
)  # 每个元素加1

print("窄依赖转换结果:", result.collect())
# 输出: [7, 9, 11, 13, 15, 17, 19, 21]

# 查看依赖关系
print("\n依赖链:")
for rdd in [result]:
    print(f"{rdd}: {rdd.toDebugString().decode()}")

sc.stop()
