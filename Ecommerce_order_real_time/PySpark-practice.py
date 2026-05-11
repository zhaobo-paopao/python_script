"""
1:PySpark核心模块
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, sum  # 导入常用函数

"""
2:创建SparkSession,这是PySpark的唯一入口
"""
import os
import sys

# 指定Python可执行文件路径（使用你的实际Python路径）
os.environ["PYSPARK_PYTHON"] = sys.executable  # 使用当前Python解释器
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


if __name__ == "__main__":
    # 构建SparkSession,本地多线程进行,应用名自定义
    spark = (
        SparkSession.builder.appName("PySpark_DF_Practice")
        .master("local[*]")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .config("spark.driver.host", "127.0.0.1")
        .getOrCreate()
    )
# 关闭冗余日志，只显示警告/错误日志
spark.sparkContext.setLogLevel("WARN")
"""
3:构建测试订单DataFrame
测试数据源：列表嵌套元组,模拟6条电商订单数据
字段:订单id,客户id,产品名称,购买数量,订单总价,订单日期
"""
order_data = [
    (1001, "c001", "手机", 2, 7998.0, "2023-02-03"),
    (1002, "c002", "电脑", 1, 5999.0, "2023-02-03"),
    (1003, "c003", "平板", 3, 8997.0, "2023-02-03"),
    (1004, "c004", "手机", 1, 3999.0, "2023-02-04"),
    (1005, "c005", "耳机", 2, 598.0, "2023-02-04"),
    (1006, "c006", "电脑", 2, 11998.0, "2023-02-04"),
]
# 定义列名(schema),和数据字段一一对应
order_schema = [
    "order_id",
    "customer_id",
    "product",
    "quantity",
    "total_amount",
    "order_date",
]
# 创建DateFrame（核心,将本地的数据转换为Spark分布式DataFrame）
df = spark.createDataFrame(data=order_data, schema=order_schema)
# 查看数据基本信息(开发测试必备,验证数据创建成功)
print("=============原始订单数据结构============")
df.printSchema()  # 打印列名+数据类型
print("=============原始订单数据内容============")
df.show(truncate=False)  # 打印所有数据，truncate=False不截断列
# ===4:DataFrame核心基础操作(select.filter,groupBy)=======
# ======= 4.1 选择指定列,按需选择字段，类似sql的select
# 需求:只保留订单id,产品，数量，总结列
df_select = df.select("order_id", "product", "quantity", "total_amount")
print("====select操作结果,只保留指定的列===========")
df_select.show()
# 进阶,select+列运算,新增临时列,(例如单价=总结/数量)
df_select_calc = df.select(
    col("order_id"),
    col("product"),
    col("quantity"),
    col("total_amount"),
    (col("total_amount") / col("quantity")).alias("unity_price"),  # 列运算+别名
)
print("=====select列运算结果,新增单价列=========")
df_select_calc.show(truncate=False)
# -----------4.2 filter：按条件过滤数据,(类似于sql的where,多条件用&/|,括号包裹)---------
# 需求1：过滤总价>50000的高价值订单
df_filter1 = df.filter(col("total_amount") > 5000)
print("==========filter操作结果(总价>5000)==========")
df_filter1.show()
# 需求2:多条件过滤,产品是电脑后者手机,且数量大于2的订单
df_filter2 = df.filter((col("product").isin(["电脑", "手机"])) & (col("quantity") >= 2))
print("===== filter操作结果2（电脑/手机 且 数量>=2） =====")
df_filter2.show(truncate=False)
# 4.3:groupBy:分组聚合(必须跟聚合函数,类似于sql的group by+聚合)
# 核心需求:按照产品名称分组，统计电商核心指标
# 聚合指标:总销量(sum(quantity)),总销售额sum(total_amount),订单数(count(order_id)),平均价格(avg(total_amount/quantity))
df_group = (
    df.groupBy("product")
    .agg(
        sum("quantity").alias("total_sales"),  # 总销量,取别名方便后续使用
        sum("total_amount").alias("total_revenue"),  # 总销售额
        count("order_id").alias("order_count"),  # 订单数(用订单id计数更准确)
        avg(col("total_amount") / col("quantity")).alias("avg_unit_price"),  # 平均单价
    )
    .orderBy(col("total_revenue").desc())
)  # 按总销售额降序排序
print("===== groupBy+聚合操作结果（按产品分析核心指标） =====")
df_group.show(truncate=False)  # 不截断列，完整显示小数
# 5:保存处理后的结果(CSV/JSON/PARQUET,重点练这个)========
# 说明：以最终的「产品聚合分析结果df_group」为例保存，保存路径为本地相对路径（自动创建文件夹）
# 核心参数,mode='overwrite'(覆盖原有文件,避免重复运行报错)
save_path = "./PySpark-practice-result"  # 本地保存根目录
# 5.1------ 保存为CSV格式(方便人工查询,需要开启header=true显示列名)--------

df_group.write.format("csv").option("header", "true").option("sep", ",").option(
    "encoding", "UTF-8"
).mode("overwrite").save(f"{save_path}/csv")

# 5.2------ 保存为JSON格式(键值对，适合程序解析)--------
df_group.write.format("json").mode("overwrite").save(
    f"{save_path}/json"
)  # 保存路径：./pyspark_practice_result/json
# 5.3------ 保存为Parquet格式（Spark主流，列式存储、压缩比高、性能好，无需指定表头）--------
df_group.write.format("Parquet").mode("overwrite").save(f"{save_path}/parquet")
print(f"\n✅ 所有结果已保存到本地目录：{save_path},包含CSV/JSON/Parquet三种格式")
# ===================== 6. 关闭SparkSession（释放资源，规范写法）=====================
spark.stop()
