```python
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
df.show()
```

    +--------+----------+--------+-------+------+------+
    |order_id|        dt| user_id|product| price|amount|
    +--------+----------+--------+-------+------+------+
    |    1001|2026-04-01|user_001|  phone|3500.0|     1|
    |    1002|2026-04-01|user_002| laptop|5800.0|     1|
    |    1003|2026-04-01|user_003|  phone|3500.0|     2|
    |    1004|2026-04-02|user_001|headset| 399.0|     1|
    |    1005|2026-04-02|user_004|  watch|1200.0|     1|
    |    1006|2026-04-02|user_002|charger|  88.0|     2|
    +--------+----------+--------+-------+------+------+
    
    


```python
# ------------------------------------------------------------------------------------------
# 关键在这里：直接写 HDFS，不需要本地保存，不需要上传！
# ------------------------------------------------------------------------------------------
hdfs_path = "hdfs://192.168.10.121:9000/test_hdfs_csv"
df.coalesce(1)\
    .write.mode('overwrite')\
    .option('header',True)\
    .csv(hdfs_path)
```


```python
# 2. 从 HDFS 读取 CSV（验证）
df_read = spark.read.option("header", True).csv(hdfs_path)
df_read.show()
```

    +--------+----------+--------+-------+------+------+
    |order_id|        dt| user_id|product| price|amount|
    +--------+----------+--------+-------+------+------+
    |    1001|2026-04-01|user_001|  phone|3500.0|     1|
    |    1002|2026-04-01|user_002| laptop|5800.0|     1|
    |    1003|2026-04-01|user_003|  phone|3500.0|     2|
    |    1004|2026-04-02|user_001|headset| 399.0|     1|
    |    1005|2026-04-02|user_004|  watch|1200.0|     1|
    |    1006|2026-04-02|user_002|charger|  88.0|     2|
    +--------+----------+--------+-------+------+------+
    
    


```python
# 3. 转 Parquet 并保存 HDFS
df_read.write.mode('overwrite').parquet('hdfs://192.168.10.121:9000/test_hdfs_parquet')
```


```python
# 4. 读取 Parquet
df_parquet=spark.read.parquet('hdfs://192.168.10.121:9000/test_hdfs_parquet')
df_parquet.show()
```

    +--------+----------+--------+-------+------+------+
    |order_id|        dt| user_id|product| price|amount|
    +--------+----------+--------+-------+------+------+
    |    1001|2026-04-01|user_001|  phone|3500.0|     1|
    |    1002|2026-04-01|user_002| laptop|5800.0|     1|
    |    1003|2026-04-01|user_003|  phone|3500.0|     2|
    |    1004|2026-04-02|user_001|headset| 399.0|     1|
    |    1005|2026-04-02|user_004|  watch|1200.0|     1|
    |    1006|2026-04-02|user_002|charger|  88.0|     2|
    +--------+----------+--------+-------+------+------+
    
    


```python
# 5. 统计分析
result=df_parquet.groupBy('product').agg({
    'price':'sum',
    'amount':'sum'
}).withColumnRenamed('sum(price)','total_sales')
result.show()
```

    +-------+-----------+-----------+
    |product|sum(amount)|total_sales|
    +-------+-----------+-----------+
    |  watch|        1.0|     1200.0|
    |  phone|        3.0|     7000.0|
    |headset|        1.0|      399.0|
    | laptop|        1.0|     5800.0|
    |charger|        2.0|       88.0|
    +-------+-----------+-----------+
    
    


```python
# 6. 结果保存回 HDFS
result.write.mode('overwrite').parquet('hdfs://192.168.10.121:9000/test_hdfs_result')
```
