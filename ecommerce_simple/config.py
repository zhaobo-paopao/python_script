# config.py - 最简单的配置
import os

# Kafka配置
KAFKA_BRKOER = os.getenv('KAFKA_BROKER', '192.168.10.121:9092')
KAFKA_TOPIC = 'ecommerce_orders'

# 数据库配置
ORACLE_CONFIG = {
    'host': 'localhost',
    'port': 1521,
    'user': 'zb',
    'password': '1',
    'service': 'orcl'
}

POSTGRES_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'postgres',
    'user': 'zhaobo',
    'password': '1'
}

# ============ Spark配置 ============
SPARK_MASTER = "local[*]"
APP_NAME = "EcommerceRealtime"
SPARK_HOME = "/home/hadoop/app/spark"
# 注意：您的Spark是2.4.8，Kafka连接器必须用Scala 2.11版本
KAFKA_CONNECTOR_PATH = "/home/hadoop/app/spark/jars/spark-sql-kafka-0-10_2.11-2.4.8.jar"
KAFKA_CLIENT_PATH = "/home/hadoop/app/spark/jars/kafka-clients-2.0.0.jar"
# ============ Web仪表盘配置 ============
WEB_HOST = "0.0.0.0"
WEB_PORT = 5000
# ============ 模拟数据配置 ============
PRODUCTS = ["iPhone 15", "MacBook Pro", "iPad Air", "AirPods Pro", "Apple Watch"]
CITIES = ["北京", "上海", "广州", "深圳", "杭州", "成都", "南京"]
CATEGORIES = ["电子产品", "家用电器", "图书", "服饰", "食品"]