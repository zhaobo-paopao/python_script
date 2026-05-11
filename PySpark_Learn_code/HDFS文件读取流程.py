import os,sys
from pyspark.sql import SparkSession
os.environ['PYSPARK_PYTHON']='python'
# 1. 创建测试数据（电商订单）
# 1. 创建电商订单数据
data = [
    (1001, "2026-04-01", "user_001", "phone", 3500.0, 1),
    (1002, "2026-04-01", "user_002", "laptop", 5800.0, 1),
    (1003, "2026-04-01", "user_003", "phone", 3500.0, 2),
    (1004, "2026-04-02", "user_001", "headset", 399.0, 1),
    (1005, "2026-04-02", "user_004", "watch", 1200.0, 1),
    (1006, "2026-04-02", "user_002", "charger", 88.0, 2),
]

# 定义列名
columns = ["order_id", "dt", "user_id", "product", "price", "amount"]
spark=SparkSession.builder\
        .appName('test_hdfs')\
        .master('local[*]')\
        .getOrCreate()
df = spark.createDataFrame(data, schema=columns)
# df.show()
# 2. 保存为 CSV 并上传 HDFS
# 2. 写入本地CSV
'''
将 DataFrame 的分区数合并为 1
coalesce() 是窄依赖转换，不会引起全量 shuffle.
但会把所有数据发送到一个分区。
目的是让最终只输出一个文件
（因为 Spark 默认每个分区写一个文件）。
将 DataFrame 中的所有数据合并成一个分区，
并以带表头的 CSV 格式覆盖写入到 /tmp/orders_csv 目录中
（最终产生一个 CSV 文件）
'''
df.coalesce(1).write.mode('overwrite').option('header',True).csv('temp/test_hdfs_csv')
# 3. 上传到 HDFS
os.system('hadoop fs -put /temp/test_hdfs_csv /test_hdfs_csv')
# 3. Spark 从 HDFS 读取 CSV
# 4. 从HDFS读取CSV
df_csv=spark.read.option('header',True)\
            .csv('hdfs://192.168.10.121:50070/test_hdfs_csv')
df_csv.show()
# 4. 转换成 Parquet 并保存到 HDFS
# 5. 转成 Parquet 写入 HDFS
df_csv.write.mode('overwrite').parquet('hdfs://192.168.10.121:50070/test_hdfs_parquet')
# 5. 从 HDFS 读取 Parquet（验证功能）
# 6. 读取Parquet
df_parquet=spark.read.parquet('hdfs://192.168.10.121:50070/test_hdfs_parquet')
df_parquet.show()

# 6. 数据分析（聚合统计）
# 7. 数据分析：按商品统计销售额、销量
df_analyze=df_parquet.groupBy('product')\
            .agg({
                'price':'sum',
                'amount':'sum'
            })\
            .withColumnRenamed('sum(price)','total_sales')\
            .withColumnRenamed('sum(amount)','total_count')
df_analyze.show()
# 7. 把分析结果保存回 HDFS
# 8. 保存分析结果到HDFS
df_analyze.write.mode('overwrite').parquet('hdfs://192.168.10.121:50070/test_hdfs_analysis_result')
