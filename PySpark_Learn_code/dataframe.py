# Python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os,sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# 创建SparkSession
spark = SparkSession.builder \
    .appName("DataFrame Example") \
    .master("local") \
    .getOrCreate()

# 创建DataFrame
data = [("Alice", 25, "NY"), ("Bob", 30, "CA"), ("Charlie", 35, "NY")]
columns = ["name", "age", "city"]
df = spark.createDataFrame(data, columns)

# 显示DataFrame
df.show()
# +-------+---+-----+
# |   name|age| city|
# +-------+---+-----+
# |  Alice| 25|   NY|
# |    Bob| 30|   CA|
# |Charlie| 35|   NY|
# +-------+---+-----+

# DataFrame操作
df.select("name", "age").show()  # 选择特定列
df.filter(col("age") > 28).show()  # 过滤
df.groupBy("city").count().show()  # 分组聚合
df.createOrReplaceTempView("people")  # 创建临时视图
spark.sql("SELECT * FROM people WHERE age > 28").show()  # SQL查询

# 关闭
spark.stop()