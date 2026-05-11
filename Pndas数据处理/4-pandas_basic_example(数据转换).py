# 使用df['列名'].astype进行数据类型转换，使用df.pivot_table进行数据重塑，使用pd.merge进行数据合并。
import pandas as pd

data = {
    'name': ['老邓','小李','小王'],
    'age': ['30','25','28'],
    'city': ['北京','上海','广州']
   }
df = pd.DataFrame(data)

# 数据类型转换
df['age'] = df['age'].astype(int)
print(df.dtypes)

# 

df_pivot = df.pivot_table(index='city', values='age', aggfunc='mean')
print(df_pivot)

# 数据合并
data2 = {'name': ['老邓','小李','小赵'],
    'gender': ['男','男','女']}
df2 = pd.DataFrame(data2)
df_merged = pd.merge(df, df2, on='name', how='left')
print(df_merged)