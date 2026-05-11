from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# 1. 创建SparkSession
spark = SparkSession.builder \
    .appName("MustSeePlan") \
    .master("local[2]") \
    .getOrCreate()

# 2. 关键：读文件（模拟真实场景，有IO）+ Join（有Shuffle）+ 聚合
# 先写一个临时csv文件（模拟数据源）
df1 = spark.createDataFrame([(1,"北京"),(2,"上海"),(3,"广州")], ["id","city"])
df1.write.mode("overwrite").csv("./test_city.csv", header=True)

# 读文件（核心：有IO操作）
df_city = spark.read.csv("./test_city.csv", header=True)
df_user = spark.createDataFrame([(1,"张三"),(1,"李四"),(2,"王五")], ["id","name"])

# Join + 聚合（核心：有执行逻辑）
df_result = df_user.join(df_city, on="id") \
                  .groupBy("city") \
                  .count()

# 执行Action（触发计算）
df_result.show()

# 3. 卡住程序，保留Spark UI
input("现在去Spark UI的SQL页面，点show那行的details，必看Physical Plan！")