# spark_streaming.py
import sys

sys.path.append(".")

from config import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    col,
    count,
    current_timestamp,
    desc,
    sum,
    to_timestamp,
    window,
)
from pyspark.sql.types import IntegerType, LongType, StringType, StructField, StructType


def create_spark_session():
    """创建Spark会话（包含Kafka连接器）"""
    spark = (
        SparkSession.builder.appName(APP_NAME)
        .master(SPARK_MASTER)
        .config("spark.jars", f"{KAFKA_CONNECTOR_PATH},{KAFKA_CLIENT_PATH}")
        .config("spark.driver.memory", "2g")
        .config("spark.executor.memory", "2g")
        .config("spark.sql.shuffle.partitions", "10")
        .config("spark.streaming.stopGracefullyOnShutdown", "true")
        .config("spark.sql.streaming.schemaInference", "true")
        .config("spark.sql.streaming.metricsEnabled", "true")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")
    return spark


def define_order_schema():
    """定义订单数据结构"""
    return StructType(
        [
            StructField("order_id", LongType()),
            StructField("customer_id", StringType()),
            StructField("product", StringType()),
            StructField("category", StringType()),
            StructField("price", IntegerType()),
            StructField("quantity", IntegerType()),
            StructField("total_amount", IntegerType()),
            StructField("city", StringType()),
            StructField("payment_method", StringType()),
            StructField("order_status", StringType()),
            StructField("order_time", StringType()),
            StructField("timestamp", LongType()),
        ]
    )


def process_streaming():
    """主处理函数"""
    print("=" * 70)
    print("🚀 Spark Structured Streaming - 电商订单实时分析")
    print("=" * 70)

    # 1. 创建Spark会话
    spark = create_spark_session()
    print(f"✅ Spark会话创建成功 | ID: {spark.sparkContext.applicationId}")
    print(f"🔗 连接Kafka: {KAFKA_BROKER}")
    print(f"📡 订阅主题: {KAFKA_TOPIC}")

    # 2. 从Kafka读取数据
    kafka_df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", KAFKA_TOPIC)
        .option("startingOffsets", "latest")
        .option("maxOffsetsPerTrigger", 100)
        .load()
    )

    schema = define_order_schema()

    # 3. 解析JSON数据
    orders_df = kafka_df.select(
        from_json(col("value").cast("string"), schema).alias("data")
    ).select("data.*")

    # 添加处理时间
    orders_df = orders_df.withColumn("processing_time", current_timestamp()).withColumn(
        "order_timestamp", to_timestamp(col("order_time"))
    )

    print("\n📊 实时分析指标计算中...")
    print("1. 实时销售额统计（每分钟）")
    print("2. 热门产品排名")
    print("3. 城市销售分布")
    print("4. 支付方式分析")
    print("5. 订单状态监控")
    print("-" * 70)

    # 4. 实时计算指标
    # 4.1 实时销售额统计（每分钟）
    sales_by_minute = (
        orders_df.withWatermark("order_timestamp", "10 minutes")
        .groupBy(window(col("order_timestamp"), "1 minute"), "category")
        .agg(
            count("*").alias("order_count"),
            sum("total_amount").alias("revenue"),
            avg("total_amount").alias("avg_order_value"),
            sum("quantity").alias("total_quantity"),
        )
        .select(
            col("window.start").alias("window_start"),
            "category",
            "order_count",
            "revenue",
            "avg_order_value",
            "total_quantity",
        )
        .orderBy(desc("window_start"), desc("revenue"))
    )

    # 4.2 热门产品排名
    product_ranking = (
        orders_df.groupBy("product", "category")
        .agg(
            count("*").alias("total_orders"),
            sum("total_amount").alias("total_revenue"),
            sum("quantity").alias("total_sold"),
            avg("price").alias("avg_price"),
        )
        .orderBy(desc("total_revenue"))
    )

    # 4.3 城市销售分布
    city_sales = (
        orders_df.groupBy("city")
        .agg(
            count("*").alias("order_count"),
            sum("total_amount").alias("total_sales"),
            countDistinct("customer_id").alias("unique_customers"),
            avg("total_amount").alias("avg_city_order"),
        )
        .orderBy(desc("total_sales"))
    )

    # 4.4 支付方式分析
    payment_analysis = (
        orders_df.groupBy("payment_method")
        .agg(
            count("*").alias("usage_count"),
            sum("total_amount").alias("total_amount"),
            (count("*") * 100.0 / orders_df.count()).alias("usage_percent"),
        )
        .orderBy(desc("usage_count"))
    )

    # 5. 输出到控制台
    print("启动流处理查询...")
    print("等待数据输入...\n")

    # 输出查询1：实时销售额
    query1 = (
        sales_by_minute.writeStream.outputMode("update")
        .format("console")
        .option("truncate", "false")
        .trigger(processingTime="30 seconds")
        .start()
    )

    # 输出查询2：热门产品
    query2 = (
        product_ranking.writeStream.outputMode("complete")
        .format("console")
        .option("truncate", "false")
        .trigger(processingTime="1 minute")
        .start()
    )

    # 输出查询3：城市分布
    query3 = (
        city_sales.writeStream.outputMode("complete")
        .format("console")
        .option("truncate", "false")
        .trigger(processingTime="1 minute")
        .start()
    )

    # 等待所有查询
    print("✅ 所有流处理查询已启动")
    print("按 Ctrl+C 停止流处理\n")

    query1.awaitTermination()
    query2.awaitTermination()
    query3.awaitTermination()


if __name__ == "__main__":
    process_streaming()
