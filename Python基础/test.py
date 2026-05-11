I=[1,2,3,4,5,6,7,8,9,10]
def fn2(i):
    if i % 2==0:
        return True
    return False
def fn3(i):
    return i%2==0
# print(fn2(5))
# print(fn3(6))
def fn(func,lst):
    new_list=[]
    for n in lst:
        if func(n):
            new_list.append(n)
    return new_list
# print(fn(fn2,I))

# 匿名函数 = lambda 函数表达式 （语法糖：简写）
#   lambda 函数表达式专门用来创建一些简单的函数，它是函数创建的又一种方式
#   语法：lambda 参数列表 : 返回值
#   匿名函数一般都是作为参数使用，其它地方一般不会使用，功能复杂时，就不要再使用匿名函数了！

def fn5(a,b):
    return a+b
# print(fn5(1,3))
# 1. 加法
add=lambda a,b:a+b
# print(add(3,5))
# 2. 平方
square=lambda x:x**2
# print(square(4))
# 3. 检查偶数
is_even=lambda i: i%2==0
# print(is_even(4))
# print(is_even(5))

# (lambda a, b : a + b)(10, 30)     # 调用匿名函数，但一般不会这么做
# 也可以将匿名函数赋值给一个变量，但一般不会这么做，相当于给函数起名字了
fn6 = lambda a, b : a + b
# print(fn6(10, 30))

# r = filter(lambda i : i > 5, l)
# print(list(r))


# def fn9(original_func):
#     def wrapper():
#         print('函数开始执行...')
#         result=original_func()
#         print('函数结束执行...')
#         return result
#     return wrapper
# @fn9
# def fn10():
#     print('hello')
# fn10()


def f1(t1):
    def fn2():
        print('开始执行')
        result=t1()
        print('结束执行')
        return result
    return fn2
@f1
def f3():
    print('装饰器开始！')
# f3()

# def fn9():
#     print('函数开始执行')
#     def fn10():
#         print('hello')
#     fn10()
#     print('函数执行结束')
# fn9()
# def make_multiplier(n):
#     def multiplier(x):
#         return x * n
#     return multiplier

# def fn1(n):
#     def warpper(n,m):
#         print('开始')
#         result=n*m
#         print('结束')
#         return result
      
        
#     return warpper
# @fn1
# def fn11():
#     print('hello')

# p=fn11(5,4)
# print(p)

# import boto3
# from pymongo import Mongoclient
# from delta import DeltaTable
# import milvus


# enumerate是Python的一个内置函数，用于将一个可遍历的数据对象
# （如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标（索引）。
# list1=['a','b','c']
# for i in range(len(list1)):
#     print(i,list1[i])

# for i,value in enumerate(list1):
#     print(i,value)
# # 如果我们希望索引从1开始，可以设置start=1：
# for i,value in enumerate(list1,start=1):
#     print(i,value)

# print(list(enumerate(list1)))






# 不使用enumerate的传统方法
fruits = ['苹果', '香蕉', '橙子', '葡萄']

# 传统方式
for i in range(len(fruits)):
    pass
    # print(f"索引{i}: {fruits[i]}")



# 使用enumerate的更简洁方式
for i, fruit in enumerate(fruits):
    pass
    
    # print(f"索引{i}: {fruit}")

# 输出相同结果

# 指定起始索引为1
fruits = ['苹果', '香蕉', '橙子', '葡萄']
fruits1 = ['苹果', '香蕉', '橙子', '葡萄','西瓜', '香蕉', '橙子','香蕉','香蕉']


for i, fruit in enumerate(fruits, start=1):
    print(f"第{i}个水果: {fruit}")
print(fruits1.index('香蕉',2,3))
# enumerate对象可以转换为列表查看

# print(list(enumerate(fruits)))


# import sys
# print(f"Python 版本: {sys.version}")
# print(f"Python 路径: {sys.executable}")
# print(f"模块搜索路径: {sys.path[:3]}")


# import sys
# print(f"当前Python路径: {sys.executable}")
# print(f"Python版本: {sys.version}")
# print(sys.executable)




import numpy as np
import pandas as pd
s=pd.Series([10,2,np.nan,None,3,4,5],index=['A','B','C','D','E','F','G'],name='data')
# print(s)
# s.count()
# # print(s.count())
# print("这是print的输出：", s.count())
print(pd.isna(s))
print(s.isin([4,5,6]))

# sales=pd.Series([120,135,145,160,155,170,180,175,190,200,210,220],index=pd.date_range('2022-01-01',periods=12,freq='ME'))
# print(sales)
# print(pd.__version__)
# print(np.__version__)

#绘制折线图
import matplotlib.pyplot as plt
#创建图表,设置大小
plt.figure(figsize=(10,5))   #宽是10高是5
#绘图的数据
month=['1月','2月','3月','4月']
sales=[100,150,80,130]
#绘制折线图
plt.plot(month,sales)
#显示图标
plt.show()