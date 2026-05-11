import pandas as pd
import numpy as np

data = {
  'name': ['老邓','小李','小王', None],
   'age': [30,25,28, np.nan],    #pandas 将 None和 np.nan都识别为缺失值
   'city': ['北京','上海','广州','深圳']
   }
df = pd.DataFrame(data)

# 处理缺失值
df_fillna = df.fillna(0) # 用0填充缺失值
print(df_fillna)

df_dropna = df.dropna() # 删除包含缺失值的行
print(df_dropna)

# 处理重复值
df_duplicated = df.drop_duplicates() # 删除重复行
print(df_duplicated)

# 使用df.fillna填充缺失值，使用df.dropna删除包含缺失值的行，使用df.drop_duplicates删除重复行。