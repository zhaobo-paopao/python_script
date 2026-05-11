# -------------------------------------------
# 第1步：启动Spark（本地运行，适配8G内存）
# 运行位置：本地 VS Code + PySpark 环境
# -------------------------------------------
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType,LongType,DateType,DoubleType,StructType,StructField
import random
import os,sys
os.environ['PYSPARK_PYTHON']='python'
spark=SparkSession.builder\
    .appName('Bank_1000W')\
    .master('local[2]')\
    .config('spark.driver.memory','6G')\
    .config('spark.sql.adaptive.enabled','True')\
    .getOrCreate()
print('Spark启动成功!!!!!!!!!!!!!!!!!!!')
# -------------------------------------------
# 第2步：生成 1000万 银行交易数据
# 运行位置：本地 VS Code
# -------------------------------------------
def generate_data():
    for i in range(1,10000001):  # 循环1000万次，生成交易数据
        yield(
            i, # 交易ID（自增主键）
            f'cust_{random.randint(10000,99999)}', # 客户ID（5位随机数）
            f'acc_{random.randint(100000,999999)}', # 账户ID（6位随机数）
            round(random.uniform(10.0, 100000.0),2),  #交易金额（10元~10万元，保留2位小数）
            random.choice(['消费', '转账', '存款', '取款', '代扣']), #交易类型
            '20260405' # 分区字段：日期
        )
# 定义dataframe的Schema
schema=StructType([
    StructField("trans_id", LongType(), True),
    StructField("cust_id", StringType(), True),
    StructField("account_id", StringType(), True),
    StructField("trans_amt", DoubleType(), True),
    StructField("trans_type", StringType(), True),
    StructField("trans_date", StringType(), True)
])
 
# 生成DataFrame
df=spark.createDataFrame(
    generate_data(),
    schema
)
print("✅ 1000万数据生成完成")
df.printSchema()
df.show(20)
# -------------------------------------------
# 第3步：写入 HDFS（核心！包含 分区 + 压缩）
# 运行位置：本地 VS Code
# -------------------------------------------
df.repartition(10)\
    .write\
    .mode('overwrite')\
    .partitionBy('trans_date')\
    .option('compression','snappy')\
    .parquet('hdfs://192.168.10.121:9000/user/bank/transaction')
print('✅ 1000万银行数据已写入 HDFS 完成！')
# -------------------------------------------
# 第4步：读取HDFS数据验证
# -------------------------------------------
df_read=spark.read.parquet('hdfs://192.168.10.121:9000/user/bank/transaction')
print(f'总共读取了:{df_read.count()}条数据---------')
df_read.show(100)