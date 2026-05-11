# 尝试求10的阶乘(10!)
# 1!= 1
# 2!= 1*2 = 2
# 3!=1*2*3 = 6
# 4!= 1*2*3*4 = 24
# 创建一个函数求任意数的阶乘
# 创建一个变量保存结果
'''
n=10
for  i in range(1,10):
    n*=i
print(n)
'''
# 创建一个函数求任意数的阶乘
'''
def fact(n):
    # n=10
    result=n
    for  i in range(1,n):
        result*=i
    return result
print(fact(5))
'''

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(10))

import math

print(math.factorial(10))  # 120