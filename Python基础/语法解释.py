'''
# range(start, end+1): 生成从start到end的数字序列
for  i in range(1,50):
    print(i)

num = 9
# 方式1：位置占位
res = "{:03d}".format(num)
print(res)  # 输出：009

name = "商品"
code = 12
msg = "{}-编号：{:03d}".format(name, code)
print(msg)  # 输出：商品-编号：012
'''


# # 2. f-string（Python 3.6+，推荐）
# # 最简洁、高效的方式，直接在字符串中嵌入表达式：
# num = 23
# # 基础用法
# res = f"{num:03d}"
# print(res)  # 输出：023

# # 结合复杂场景（如循环生成序号）
# for i in range(5):
#     # print(i)
#     print(f"第{i+1:03d}条数据")
#     # print(f'第{i+1:03d}条数据!')
#     # print(f'第{i+1:03d}条数据')
# # 输出：
# # 第001条数据
# # 第002条数据
# # 第003条数据
# # 第004条数据
# # 第005条数据
'''
# 字典和序列转换
import pprint
kafka_config={'bootstrap_servers':'192.168.10.121:9092','topic':'lick-stream','group_id':'lick-analytics-group'}
print(kafka_config['bootstrap_servers'])
print(list(kafka_config.values())[0])
print(list(kafka_config.values())[0])

GENERATOR_CONFIG = {
    'events_per_second': 2,      # 每秒生成事件数,数据生成速率
    'total_events': 100,         # 总共生成100个事件后停止
    'users_range': (1, 50),      # 用户ID范围,用户ID从1到50随机选择，模拟50个不同用户
    'products': [                # 商品列表 ，苹果15,笔记本,T恤,书,咖啡
        {'id': 'P001', 'name': 'iPhone 15', 'category': 'Electronics', 'price': 7999},
        {'id': 'P002', 'name': 'Laptop', 'category': 'Electronics', 'price': 5999},
        {'id': 'P003', 'name': 'T-Shirt', 'category': 'Clothing', 'price': 199},
        {'id': 'P004', 'name': 'Book', 'category': 'Books', 'price': 59},
        {'id': 'P005', 'name': 'Coffee', 'category': 'Food', 'price': 35}
    ]
}

products=GENERATOR_CONFIG['products']
print(type(products))
print(products)
'''
'''

# random.choice()随机数选择
import random
# class UserSelector():
#     def __init__(self) -> None:
#          # 初始化实例属性users（序列类型，比如列表）
#         self.name=['张三','李四','王五','赵六']
#     def get_random_user(self):
#         user=random.choices(self.name)
#         return user
# selector=UserSelector()
# print(selector.get_random_user())

# random.choice() 的约束
# 入参必须是「序列」（列表、元组、字符串、range 等），不能是字典（字典需转成 list(dict.keys())/list(dict.values())）；
# 入参不能为空（比如空列表 []），否则报错；
# 选中每个元素的概率相等（均匀随机）。
    
# 若想随机选多个不重复元素：用 random.sample(self.users, k=2)（选 2 个）；
# 若想打乱序列后取第一个：random.shuffle(self.users); user = self.users[0]；
# 若想带权重随机选择：需借助 random.choices()（注意是复数）：  
# user = random.choice(self.users) 的核心语法逻辑是：
# 在类的方法中，从当前实例的 users 序列属性里，随机选取一个元素并赋值给 user 变量。
# 核心依赖 random 模块的 choice 函数，且 self.users 必须是非空序列。
# random 相对权重（weights）—— 最常用
# 需求：张三权重 1，李四权重 2，王五权重 7 → 总权重 = 1+2+7=10
class UserName():
    def __init__(self) -> None:
        self.users=['张三','李四','王五']
    def get_random_user(self):
        # 带相对权重选取5个元素（允许重复）
        users=random.choices(self.users,weights=[1,3,6],k=5)
        return users
getname=UserName()
print(getname.get_random_user())

'''

'''
# f-string 基础语法
import time
import os
from datetime import datetime
import random
from config import GENERATOR_CONFIG
name='Alice'
age=25
# t=int(time.time()*1000)
# id=i'EV{int(time.time() * 1000)}'
id=int(time.time()*1000)
# print(f'名字叫:{name}',f'年龄是:{age}')
result=f'EV{id}'
print(time.time())
print(result)
product = GENERATOR_CONFIG['products']  # 从配置导入商品

# print(t)
event = {
            'event_id': f'EV{int(time.time() * 1000)}', # 唯一事件ID，基于时间戳
            'user_id': 'user',
            'product_id': 'product',
            'product_name': 'productname',
            'timestamp': datetime.now().isoformat(),   # ISO格式时间
            'session_id': f'SESS{random.randint(1000, 9999)}', # 会话ID
        }
print(event['event_id'],event['timestamp'],event['session_id'])

'''