# num=10
# for i in range(num):
#  print(i)


# try:
#     number = 10
#     for i in number:  # 尝试迭代整数，将引发TypeError
#         print(i)
# except TypeError as e:
#     print(f"捕获到TypeError: {e}")
    
#from collections import Iterable  #使用迭代器,需要导入
from collections.abc import Iterable   #Iterable是Python 3.3及以上版本中collections.abc模块的一部分,所以应该以这种方式引入Iterable
number=10
if isinstance(number,Iterable):  #判断是否为可迭代对象
        for i in number:
            print(i)
else:
            print("该变量不可迭代")

# from collections.abc import Iterable
# number = 10
# if isinstance(number, Iterable):  # 检查是否为可迭代类型
#     for i in number:
#         print(i)
# else:
#     print("变量不是可迭代的")           
