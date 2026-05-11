import pandas as pd

data = {
    'name': ['老邓','小李','小王'],
    'age': [30,25,28],
    'city': ['北京','上海','广州']
   }
df = pd.DataFrame(data)

# 选择列
names = df['name']
print(names)

# 选择行
first_row = df.iloc[0] # 选择第一行 通过整数位置选择行/列
print(first_row)






# 条件过滤
filtered_df = df[df['age'] >27]
print(filtered_df)

'''
1. df.iloc[0] 获取第0行（第一行）
2. 返回一个Series对象
3. 列名成为Series的索引
4. 单元格值成为Series的值
'''
'''

'''