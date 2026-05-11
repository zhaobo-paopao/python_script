# 示例2：在柱状图中添加数据标签
import matplotlib.pyplot as plt
import pandas as pd

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
data = {'city': ['北京', '上海', '广州', '深圳', '杭州'],
        'sales': [100, 200, 150, 180, 120]}
df = pd.DataFrame(data)

# 创建图表
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 不使用enumerate
ax1 = axes[0]
df.plot(x='city', y='sales', kind='bar', ax=ax1, legend=False)
ax1.set_title('无标签')
ax1.set_ylabel('销售额')

# 使用enumerate添加数据标签
ax2 = axes[1]
df.plot(x='city', y='sales', kind='bar', ax=ax2, legend=False)
ax2.set_title('有数据标签')
ax2.set_ylabel('销售额')

# 使用enumerate在柱子上方添加数值标签
for i, v in enumerate(df['sales']):
    ax2.text(i, v + 3, str(v), ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()