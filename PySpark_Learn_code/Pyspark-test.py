# ----------------1:导入Pyspark核心模块-----------------
# SparkSession：Pyspark的入口,相当于大数据工具箱的钥匙,必须创建
import os
# 强制指定你当前虚拟环境的 Python 路径
os.environ['PYSPARK_PYTHON']='python'
from pyspark.sql import SparkSession
# ----------------2:导创建Spark会话-----------------
# .builder:构建器模式
# .appName('MyFirstPySpark'):程序名字
# .getOrCreate():如果有会话就用,没有就新建
spark=SparkSession.builder.appName('MyFirstPySpark').getOrCreate()
print('Pyspark 启动成功！！！！')
# ===================== 3. 创建测试数据（模拟数据） =====================
# 列表套元组：数据格式 (姓名, 年龄, 城市, 成绩)
data=[
    ("张三", 20, "北京", 85),
    ("李四", 18, "上海", 92),
    ("王五", 22, "北京", 78),
    ("赵六", 19, "深圳", 90),
    ("钱七", 21, "上海", 88)
]
# 定义列名（和数据一一对应）
columns=['name','age','city','score']
# ===================== 4. 创建 Spark DataFrame（核心数据结构） =====================
# spark.createDataFrame:把普通python对象转化为分布式大数据对象
# 第一个参数:数据。第二个参数：列名
df=spark.createDataFrame(data,columns)
# ===================== 5. 基础操作：查看数据 =====================
# ❌ 不能用 print(df)：PySpark 是懒执行，不会直接打印
# ✅ 必须用 .show()：展示前20行数据（最常用打印方法）
print('===== 原始数据 =====')
df.show()   
# 操作3：按城市分组，统计每个城市的人数、平均成绩
# groupBy(列名):分组
# .count():统计数量
# .avg(列名):计算平均值
group_df=df.groupBy('city').agg({'score':'avg','name':'count'})
print("\n===== 按城市分组统计 =====")
group_df.show()
# 操作4：排序（按成绩降序）
# orderBy(列名)：排序，ascending=False 表示降序
sort_df=df.orderBy(df.score,ascending=False)
print("\n===== 按成绩降序排列 =====")
sort_df.show()
# 操作5：选择指定列（只看姓名+成绩）
select_df=df.select('name','score')
print("\n===== 只显示姓名和成绩 =====")
select_df.show()
# ===================== 7. 数据保存（把结果存成文件） =====================
# 保存为 CSV 文件（header=True 保留列名）
df.write.csv("result.csv", header=True, mode="overwrite")

# ===================== 8. 关闭 Spark 会话（程序结束必写） =====================
# 释放资源，固定收尾操作
spark.stop()
print("\n✅ PySpark 程序运行完毕！")
