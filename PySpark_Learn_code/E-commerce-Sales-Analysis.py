import os

os.environ["PYSPARK_PYTHON"] = "python"
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("EcommerceSalesAnalysis").getOrCreate()
print("EcommerceSalesAnalysis-Pyspark start successful")
# 1. Create PySpark/scala DataFrames for both the sales and products data.
# sales_data
sales_data = [
    (1, 101, "2025-01-15", 2),
    (2, 102, "2025-01-17", 1),
    (3, 101, "2025-02-10", 1),
    (4, 103, "2025-02-20", 3),
    (5, 104, "2025-03-05", 1),
    (6, 101, "2025-03-12", 3),
    (7, 102, "2025-04-01", 2),
    (8, 105, "2024-12-20", 5),
    (9, 103, "2025-05-21", 2),
    (10, 104, "2025-05-30", 4),
]
# products_data
products_data = [
    (101, "Laptop", "Electronics", 1200),
    (102, "Mouse", "Electronics", 25),
    (103, "T-Shirt", "Apparel", 20),
    (105, "Jeans", "Apparel", 75),
    (105, "Book", "Books", 15),
]
# sales_data_columns
sales_data_columns = ["sale_id", "product_id", "sale_date", "quantity"]
# products_data_columns
products_data_columns = ["product_id", "product_name", "category", "price"]
df_sales = spark.createDataFrame(sales_data, sales_data_columns)
df_products = spark.createDataFrame(products_data, products_data_columns)
df_sales.show()
df_sales.info
df_products.show()
# 2:Filter the sales data to include only records from the year 2025.
# df_sales.filter(df_sales.sale_date=='2025-01-15')
date_2025 = df_sales.filter(df_sales.sale_date.like("%2025"))
date_2025.show()
