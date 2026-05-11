# 分组 TopN（每个组内取前 N）
from pyspark.sql import Window,SparkSession
from pyspark.sql.functions import row_number
import os,sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# 创建SparkSession对象
spark=SparkSession.builder\
      .appName('GroupTopNExample')\
      .master('local[*]')\
      .getOrCreate()
#构造函数
df=spark.createDataFrame([
    ("家电", "冰箱", 500),
    ("家电", "电视", 800),
    ("家电", "空调", 700),
    ("手机", "苹果", 1500),
    ("手机", "华为", 1200),
    ("手机", "小米", 900)
],["category", "product", "sales"])
print('原始数据：')
df.show()
# 分组TopN - 每个组内取前N个
# 创建窗口函数，按category分组，按sales降序排列
window=Window.partitionBy('category').orderBy(df['sales'].desc())
# 添加排名列
df_rank=df.withColumn('rank',row_number().over(window))
print("添加排名后的数据:")
df_rank.show()
# 4. 每个组取 Top2
topN_per_group =df_rank.filter('rank<=2')
print('每个组取 Top2:')
topN_per_group.show()