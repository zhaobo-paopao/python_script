from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
from  pyspark.sql.functions import col,rand,lit,when,concat_ws
import os,sys
#创建Spark会话
# 本地四核运行 master('local[4]')
# 给主进程4核内存 config('spark.driver.memory','4g')
# 安全创建或者复用Spark入口
# 1. 强制指定Python解释器路径
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark=SparkSession.builder\
    .appName('SkewDataPractice')\
        .master('local[4]')\
            .config('spark.driver.memory','4g')\
              .config("spark.driver.host", "127.0.0.1") \
                .config("spark.driver.bindAddress", "127.0.0.1") \
                  .getOrCreate()
print('✅️Spark启动成功,开始生成测试数据...')
#生成倾斜数据的函数
def generate_skewed_data(num_records=1000000,skew_factor=100,hot_keys_count=5):
    '''
    生成有倾斜特征的数据
    参数:
    -num_records:总记录数
    -skew_factor:倾斜因子(热点key的记录数是普通key的多少倍)
    -hot_keys_count:热点key的数量
    返回:包含倾斜Key的DataFrame
    '''
    print(f'生成{num_records}条纪录,其中{hot_keys_count}个热点key..')
    #生成热点key(占总数的80%)
    hot_records=int(num_records*0.8)
    normal_records=num_records-hot_records
    #创建热点key数据
    hot_keys=[f'hot_key_{i}' for i in range(hot_keys_count)]
    hot_data=[]
    #每个热点key分配大致相同的记录数
    records_per_hot_key=hot_records//hot_keys_count
    for hot_key in hot_keys:
        for _ in range(hot_keys_count):
            amount=np.random.uniform(100,10000) #随机金额
            hot_data.append((hot_key,amount))
    #创建普通key数据
    normal_keys_count=1000 # 1000个普通key
    normal_keys=[f'normal_key_{i}' for i in range(normal_keys_count)]
    normal_data=[]
    records_per_normal_key=normal_records//normal_keys_count

    for normal_key in normal_keys:
        for _ in range(records_per_normal_key):
            amount=np.random.uniform(10,1000)  # 普通key金额较小
            normal_data.append((normal_key,amount))
    #合并数据
    all_data=hot_data+normal_data
    #转换为Spark DataFrame
    columns=['key','amount']
    df=spark.createDataFrame(all_data,columns)
        #添加一些额外字段
    from pyspark.sql.functions import current_timestamp,expr
    df=df.withColumn('timestamp',current_timestamp())\
        .withColumn('category',
                    when(col('key').startswith('hot'),'premium')
                    .otherwise('standard'))
    print(f"✅ 生成完成！数据分布：")
    print(f"   - 总记录数: {df.count():,}")
    print(f"   - 热点key数: {hot_keys_count}")
    print(f"   - 每个热点key约 {records_per_hot_key:,} 条记录")
    print(f"   - 普通key数: {normal_keys_count}")
    print(f"   - 每个普通key约 {records_per_normal_key:,} 条记录")
    return df
df_big_table=generate_skewed_data(num_records=100000,skew_factor=100,hot_keys_count=3)
print('\n大表数据示例:')
df_big_table.show(100)
#生成小表数据
def generate_small_table():
    '''生成小表,维度表'''
    #创建热点key的详细信息
    hot_keys_info=[]
    for i in range(3):
        hot_keys_info.append((f'hot_key_{i}',f'VIP客户{i}','北京',1000000+i*10000))
     # 创建普通key的详细信息
    normal_keys_info = []
    for i in range(1000): # 与普通key对应
        normal_keys_info.append((f"normal_key_{i}", f"普通客户{i}", "上海", 10000 + i*100))
    all_keys_info=hot_keys_info+normal_keys_info
    #转换为DateFrame
    columns=['key','customer_name','city','credit_limit']
    df_small=spark.createDataFrame(all_keys_info,columns)
    print(f"✅ 小表生成完成！记录数: {df_small.count():,}")
    print("小表示例：")
    df_small.show(10)
    return df_small
df_small_table = generate_small_table()
# 二、保存测试数据
# 保存为本地文件
def save_test_data(df_big, df_small, base_path="./test_data"):
    """保存测试数据到本地文件"""
    import os
    import shutil
    
    # 删除已存在的目录
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
        print(f"已清理旧目录: {base_path}")
    
    # 保存大表
    big_table_path = os.path.join(base_path, "big_table")
    print(f"保存大表到: {big_table_path}")
    df_big.write.mode("overwrite").parquet(big_table_path)
    
    # 保存小表
    small_table_path = os.path.join(base_path, "small_table")
    print(f"保存小表到: {small_table_path}")
    df_small.write.mode("overwrite").parquet(small_table_path)
    
    # 保存为CSV（便于查看）
    csv_big_path = os.path.join(base_path, "big_table_csv")
    print(f"保存大表CSV到: {csv_big_path}")
    df_big.limit(1000).write.mode("overwrite").csv(csv_big_path, header=True)
    
    csv_small_path = os.path.join(base_path, "small_table_csv")
    print(f"保存小表CSV到: {csv_small_path}")
    df_small.write.mode("overwrite").csv(csv_small_path, header=True)
    
    # 统计文件大小
    def get_folder_size(folder):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size
    
    print("\n📁 数据保存完成：")
    print(f"大表Parquet大小: {get_folder_size(big_table_path)/1024/1024:.2f} MB")
    print(f"小表Parquet大小: {get_folder_size(small_table_path)/1024/1024:.2f} MB")
    
    return base_path

# 保存数据
data_path = save_test_data(df_big_table, df_small_table)
# 三、加载测试数据
def load_test_data(data_path="./test_data"):
    """加载测试数据"""
    print("加载测试数据...")
    
    big_table_path = os.path.join(data_path, "big_table")
    small_table_path = os.path.join(data_path, "small_table")
    
    df_big_loaded = spark.read.parquet(big_table_path)
    df_small_loaded = spark.read.parquet(small_table_path)
    
    print(f"✅ 加载完成！")
    print(f"大表记录数: {df_big_loaded.count():,}")
    print(f"小表记录数: {df_small_loaded.count():,}")
    
    return df_big_loaded, df_small_loaded

# 加载数据
df_big, df_small = load_test_data(data_path)
# 数据倾斜分析工具
from pyspark.sql.functions import col, count, desc, max, min, avg
def analyze_data_skew(df, key_column, top_n=20):
    """分析数据倾斜情况"""
    from pyspark.sql.functions import count, col, desc
    
    print(f"\n🔍 分析 {key_column} 列的倾斜情况...")
    
    # 统计每个key的记录数
    key_stats = df.groupBy(key_column).agg(
        count("*").alias("record_count")
    ).orderBy(desc("record_count"))
    
    # 显示前top_n个最多的key
    print(f"前{top_n}个最多的key：")
    key_stats.show(top_n)
    
    # 计算倾斜度
    stats = key_stats.agg(
         max("record_count").alias("max_count"),
        min("record_count").alias("min_count"),
        avg("record_count").alias("avg_count")
    ).collect()[0]
    
    max_count = stats["max_count"]
    min_count = stats["min_count"]
    avg_count = stats["avg_count"]
    
    skew_ratio = max_count / avg_count if avg_count > 0 else float('inf')
    
    print(f"\n📊 倾斜度分析：")
    print(f"  最多记录数: {max_count:,}")
    print(f"  最少记录数: {min_count:,}")
    print(f"  平均记录数: {avg_count:.2f}")
    print(f"  倾斜比率: {skew_ratio:.2f} 倍")
    
    if skew_ratio > 10:
        print(f"严重倾斜！倾斜比率为 {skew_ratio:.2f}")
    elif skew_ratio > 3:
        print(f"中度倾斜，倾斜比率为 {skew_ratio:.2f}")
    else:
        print(f"倾斜不明显，倾斜比率为 {skew_ratio:.2f}")
    
    return key_stats

# 分析大表的key分布
key_stats = analyze_data_skew(df_big, "key")
# 场景1：普通Join（会触发倾斜问题）
def practice_regular_join():
    """练习普通Join，观察倾斜问题"""
    print("\n" + "="*60)
    print("场景1：普通Join操作")
    print("="*60)
    
    from pyspark.sql.functions import col
    import time
    
    print("执行普通Join...")
    start_time = time.time()
    
    try:
        result = df_big.join(df_small, on="key", how="inner")
        result_count = result.count()
        elapsed_time = time.time() - start_time
        
        print(f"✅ Join完成！结果记录数: {result_count:,}")
        print(f"⏱️  耗时: {elapsed_time:.2f}秒")
        
        # 查看结果示例
        print("\n结果示例：")
        result.show(10)
        
    except Exception as e:
        print(f"❌ Join失败: {e}")
        print("这可能是因为数据倾斜导致内存溢出！")
    
    return result if 'result' in locals() else None
# 场景2：广播Join（小表广播）
def practice_broadcast_join():
    """练习广播Join"""
    print("\n" + "="*60)
    print("场景2：广播Join优化")
    print("="*60)
    
    from pyspark.sql.functions import broadcast
    import time
    
    print("检查小表大小...")
    # 估算小表大小
    small_table_size = df_small.rdd.map(lambda x: len(str(x))).sum()
    print(f"小表大小约: {small_table_size/1024:.2f} KB")
    
    if small_table_size < 10 * 1024 * 1024:  # 小于10MB
        print("✅ 小表可以广播")
        
        print("\n执行广播Join...")
        start_time = time.time()
        
        result = df_big.join(broadcast(df_small), on="key", how="inner")
        result_count = result.count()
        elapsed_time = time.time() - start_time
        
        print(f"✅ 广播Join完成！结果记录数: {result_count:,}")
        print(f"⏱️  耗时: {elapsed_time:.2f}秒")
        
        return result
    else:
        print("❌ 小表太大，不适合广播")
        return None
import time  # 添加这行
from pyspark.sql.functions import col, count, avg, lit, concat, explode, array, monotonically_increasing_id

def practice_salted_join(num_salts=10):
    """练习加盐打散处理数据倾斜 - 修复列不匹配问题"""
    print(f"\n=== 练习加盐打散 (num_salts={num_salts}) ===")
    start_time = time.time()
    
    # 加载数据
    df_big, df_small = load_test_data("./skew_practice_data")
    
    # 识别热点key
    from pyspark.sql.functions import col, count, avg
    
    key_stats = df_big.groupBy("key").agg(count("*").alias("record_count"))
    avg_count = key_stats.agg(avg("record_count")).collect()[0][0]
    
    # 找真正的热点key（hot_key_0, hot_key_1, hot_key_2）
    hot_keys = ['hot_key_0', 'hot_key_1', 'hot_key_2']
    
    print(f"识别到热点key: {hot_keys}")
    
    # 对小表加盐
    from pyspark.sql.functions import lit, concat, explode, array, monotonically_increasing_id
    
    # 创建盐值列表
    salts = [lit(i) for i in range(num_salts)]
    
    # 对小表加盐
    df_small_salted = df_small.withColumn("salt", explode(array(*salts)))
    df_small_salted = df_small_salted.withColumn(
        "salted_key", 
        concat(col("key"), lit("_"), col("salt").cast("string"))
    )
    
    # 处理大表热点key
    df_big_hot = df_big.filter(col("key").isin(hot_keys))
    df_big_hot = df_big_hot.withColumn(
        "salt", 
        (monotonically_increasing_id() % num_salts).cast("int")
    )
    df_big_hot = df_big_hot.withColumn(
        "salted_key", 
        concat(col("key"), lit("_"), col("salt").cast("string"))
    )
    
    # 处理大表非热点key
    df_big_normal = df_big.filter(~col("key").isin(hot_keys))
    df_big_normal = df_big_normal.withColumn("salted_key", col("key"))
    
    # 分别进行Join - 确保两个结果有相同的列
    print("进行热点keyJoin...")
    hot_result = df_big_hot.alias("b").join(
        df_small_salted.alias("s"),
        col("b.salted_key") == col("s.salted_key")
    ).select(
        col("b.key").alias("key"),
        col("b.amount").alias("amount"),
        col("b.category").alias("category"),
        col("s.customer_name").alias("customer_name"),
        col("s.city").alias("city"),
        col("s.credit_limit").alias("credit_limit"),
        col("b.timestamp").alias("timestamp")
    )
    
    print("进行非热点keyJoin...")
    normal_result = df_big_normal.alias("b").join(
        df_small.alias("s"),
        col("b.key") == col("s.key")
    ).select(
        col("b.key").alias("key"),
        col("b.amount").alias("amount"),
        col("b.category").alias("category"),
        col("s.customer_name").alias("customer_name"),
        col("s.city").alias("city"),
        col("s.credit_limit").alias("credit_limit"),
        col("b.timestamp").alias("timestamp")
    )
    
    # 检查列数
    print(f"normal_result 列数: {len(normal_result.columns)}")
    print(f"hot_result 列数: {len(hot_result.columns)}")
    print(f"normal_result 列: {normal_result.columns}")
    print(f"hot_result 列: {hot_result.columns}")
    
    # 合并结果
    print("合并结果...")
    final_result = normal_result.union(hot_result)
    
    result_count = final_result.count()
    elapsed_time = time.time() - start_time
    
    print(f"\n✅ 加盐Join完成！")
    print(f"   结果行数: {result_count:,}")
    print(f"   耗时: {elapsed_time:.2f}秒")
    
    return final_result   
# 六、完整的练习脚本
# 完整的数据倾斜练习脚本
def full_practice_session():
    """完整的数据倾斜练习会话"""
    print("🚀 开始数据倾斜练习...")
    print("="*70)
    
    # 1. 生成测试数据
    print("步骤1: 生成测试数据")
    df_big = generate_skewed_data(num_records=100000, hot_keys_count=3)
    df_small = generate_small_table()
    
    # 2. 保存数据
    print("\n步骤2: 保存测试数据")
    data_path = save_test_data(df_big, df_small, "./skew_practice_data")
    
    # 3. 加载数据
    print("\n步骤3: 加载测试数据")
    df_big, df_small = load_test_data(data_path)
    
    # 4. 分析数据倾斜
    print("\n步骤4: 分析数据倾斜")
    analyze_data_skew(df_big, "key")
    
    # 5. 练习各种Join方法
    print("\n步骤5: 练习各种Join方法")
    
    # 5.1 普通Join
    result_regular = practice_regular_join()
    
    # 5.2 广播Join
    result_broadcast = practice_broadcast_join()
    
    # 5.3 加盐打散
    result_salted = practice_salted_join(num_salts=10)
    
    # 6. 性能对比
    print("\n" + "="*70)
    print("📊 性能对比总结")
    print("="*70)
    
    # 这里可以添加性能对比逻辑
    # 注意：由于我们模拟了执行时间，实际需要真正执行后才能对比
    
    print("练习完成！您已经体验了：")
    print("1. 生成倾斜数据")
    print("2. 分析数据分布")
    print("3. 普通Join（可能遇到问题）")
    print("4. 广播Join优化")
    print("5. 加盐打散处理倾斜")
    
    return {
        "regular_join": result_regular,
        "broadcast_join": result_broadcast,
        "salted_join": result_salted
    }

# 运行完整练习
results = full_practice_session()
input("按回车关闭程序：")