from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,split,col
import os,sys
os.environ['PYSPARK_PYTHON']=sys.executable
os.environ['PYSPARK_DRIVER_PYTHON']=sys.executable
# ====================
# 1. 创建 SparkSession
# ====================
spark=SparkSession.builder\
    .appName('WordCountDF')\
    .master('local[*]')\
    .getOrCreate()
# ====================
# 2. 构造数据
# ====================
df=spark.createDataFrame([
    ("hello spark",),
    ("hello python",),
    ("spark spark",)
],['line']) # 一列，名字叫 line
print('==== 原始数据 ===="')
df.show()
# ==============================================
# 写法 1：DataFrame 算子版（最常用）
# ==============================================
wordCountDf=df.select(
    # 把 line 按空格切开 → 炸开成一行一个单词
    explode(split(col('line'),' ')).alias('word')
).groupBy('word').count() # 分组计数
print("==== DataFrame 版 WordCount 结果 ====")
wordCountDf.show()
# ==============================================
# 写法 2：SQL 版（写 SQL 语句）
# ==============================================
df.createOrReplaceTempView('word_table')   # 建临时表
sqlResult=spark.sql(
'''
select word,count(*) as count
from (
   select explode(split(line,' ')) as word from word_table
) t
group by word
'''
)
print("==== SQL 版 WordCount 结果 ====")
sqlResult.show()
spark.stop()
