# 介绍：Pandas可以与Matplotlib等可视化库结合，将数据可视化，更直观地展示数据分析结果。
import pandas as pd
import matplotlib.pyplot as plt
# 添加中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
data = {'city': ['北京','上海','广州'],
   'sales': [100,200,150]}
df = pd.DataFrame(data)

# 数据可视化
'''
    x='city',       # X轴：城市名
    y='sales',      # Y轴：销售额
    kind='bar'      # 图表类型：柱状图
'''
df.plot(x='city', y='sales', kind='bar')
plt.show()