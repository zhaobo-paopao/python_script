#通过模块可以对python进行扩展
from time import*
# 获取程序开始时间
start=time()
i=2
while i<100:
    # 创建一个 变量,纪录i的状态,默认i是质数
    Flag=True
    # 判断i是否是质数,
    # 获取所有可能成为i的因数的数
    j=2
    while j<=i**0.5:
        # 判断i能否被j整除
        if i%j==0:
            # i能被j整除,证明i不是质数,修改Flag为False
            Flag=False
            # 一旦进入判断,证明i一定不是质数,此时内层循环没有继续执行的必要
            # 使用break来退出
            break
        j+=1
        # 验证结果并输出
    if Flag:
            print(i)
    i+=1
    # 获取程序结束时间
end=time()
print('程序执行花费了',end-start,'秒')