import os,sys
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StringType,IntegerType,DateType,DoubleType,StructField
os.environ['PYSPARK_PYTHON']='python'
spark=SparkSession.builder\
        .appName('PracticalExample')\
        .master('local')\
        .getOrCreate()
#定义Schema
sales_schema=StructType([
    StructField('sale_id',IntegerType(),True,{'decription':'销售纪录的唯一标识'}),
    StructField('product_id',IntegerType(),True,{"decription": "产品ID"}),
    StructField('sale_date',DateType(),True,{'decription':'销售日期,格式yyyy-MM-dd'}),
    StructField('quantity',IntegerType(),True,{'decription':'销售数量'})
    
])
products_schema=StructType([
    StructField('product_id',IntegerType(),True,{'decription':'销售产品的唯一标识'}),
    StructField('product_name',StringType(),True,{"decription": "产品名称"}),
    StructField('category',StringType(),True,{'decription':'产品种类'}),
    StructField('price',IntegerType(),True,{'decription':'销售价格'})
    
])
#  从本地CSV文件读取sales_data
sales_f=spark.read\
        .option('header',True)\
        .option('sep','\t')\
        .option('dateFormat','yyyy-MM-dd')\
        .schema(sales_schema)\
        .csv('C:\\Users\\60403\\Desktop\\20260312\\sales_data.csv')
print('sales_data:')
sales_f.show()
print("使用自定义schema读取销售数据:")
print(sales_f.printSchema())


# 从本地CSV文件读取products_data
products_f=spark.read\
        .option('header',True)\
        .option('sep','\t')\
        .option('dateFormat','yyyy-MM-dd')\
        .schema(products_schema)\
        .csv('C:\\Users\\60403\\Desktop\\20260312\\products_data.csv')
print('products_data:')
products_f.show()
print("使用自定义schema读取产品数据:")
print(products_f.printSchema())







# products_df=spark.read.option('header',True).option('inFerSchema',True).option('sep','\t')\
#         .csv('C:\\Users\\60403\\Desktop\\20260312\\products_data.csv')
# print('products_data')
# products_df.show()
# print(sales_f.schema["sale_id"].dataType)
# print(sales_f.schema["product_id"].dataType)
# print(sales_f.schema["sale_date"].dataType)
# print(sales_f.schema["quantity"].dataType)
# print(sales_f.printSchema())
# print(products_df.printSchema())
