import os
import sys
from operator import add

from pyspark import SparkConf, SparkContext

os.environ["PYSPARK_PYTHON"] = sys.executable

# 创建 Spark 上下文
conf = SparkConf().setAppName("WideDependency").setMaster("local")
sc = SparkContext(conf=conf)

# 创建键值对 RDD
data = [("a", 1), ("b", 2), ("a", 3), ("b", 4), ("c", 5)]
rdd = sc.parallelize(data, 3)  # 3个分区

# 窄依赖操作
mapped = rdd.map(lambda x: (x[0], x[1] * 2))

# 宽依赖操作：groupByKey 需要 Shuffle
grouped = mapped.groupByKey()  # 宽依赖！
grouped_result = grouped.mapValues(lambda values: list(values)).collect()
print("groupByKey 结果:", grouped_result)
# 输出: [('a', [2, 6]), ('b', [4, 8]), ('c', [10])]

# 另一个宽依赖：reduceByKey
reduced = mapped.reduceByKey(add)  # 宽依赖！
print("reduceByKey 结果:", reduced.collect())
# 输出: [('a', 8), ('b', 12), ('c', 10)]

# 查看依赖关系
print("\ngroupByKey 的依赖:")
for rdd in [grouped]:
    print(f"{rdd}: {rdd.toDebugString().decode()}")

sc.stop()
