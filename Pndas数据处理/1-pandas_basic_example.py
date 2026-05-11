"""
=== pandas基础示例解析 ===
创建日期: 202
作者: 我自己
1. DataFrame: 二维表格
2. Series: 一维数组
3. 核心概念:
   - 用字典创建DataFrame
   - 每列是一个Series
   - 自动生成索引
"""
核心要点 = {
    "DataFrame": "二维表格，类似Excel工作表",
    "Series": "一维数组，DataFrame的列",
    "创建方式": "用字典{列名: 数据列表}",
    "索引": "自动生成0,1,2...，可自定义",
    "数据操作": "通过列名和索引访问"
}

# import pandas：导入名为 pandas 的 Python 库

# as pd：给 pandas 起个别名 pd，这样写代码时只需输入 pd.而不是 pandas.

# 作用：pandas 是一个用于数据处理和分析的第三方库
import pandas as pd

# 创建DataFrame
# 创建了一个字典 data，包含3个键值对：
# 'name'对应列表 ['老邓','小李','小王']
# 'age'对应列表 [30,25,28]
# 'city'对应列表 ['北京','上海','广州']
# 每个键将成为 DataFrame 的列名
# 每个值（列表）将成为对应列的数据
data = {'name': ['老邓','小李','小王'],
        'age': [30,25,28],
        'city': ['北京','上海','广州']
       }
df = pd.DataFrame(data)
# pd.DataFrame()：pandas 的 DataFrame 构造函数
# •
# 参数：将上面创建的字典 data传给它
# •
# 作用：创建一个二维表格（DataFrame）
# •
# 赋值：将这个表格对象赋值给变量 df
# 创建后的表格结构：
print(df)

# 创建Series
ages = pd.Series([30,25,28], name='age')
# pd.Series()：pandas 的 Series 构造函数
# •
# 第一个参数：列表 [30,25,28]是要存储的数据
# •
# name='age'：给这个 Series 命名，名字是 'age'
# •
# 作用：创建一个一维数组（Series）
# •
# 赋值：赋值给变量 ages
# 创建的 Series：
print(ages)
'''
DataFrame 结构
变量名: df
类型: pandas DataFrame
内存表示:
    ┌───────┬─────┬─────┬────────┐
索引│ (索引)│ name│ age │ city   │
    ├───────┼─────┼─────┼────────┤
    │   0   │ 老邓│  30 │ 北京   │
    │   1   │ 小李│  25 │ 上海   │
    │   2   │ 小王│  28 │ 广州   │
    └───────┴─────┴─────┴────────┘
形状: 3行 × 3列
'''
'''
变量名: ages
类型: pandas Series
内存表示:
    ┌───────┬──────┐
索引│ (索引)│ 值    │
    ├───────┼──────┤
    │   0   │  30  │
    │   1   │  25  │
    │   2   │  28  │
    └───────┴──────┘
名称: age
长度: 3
'''
