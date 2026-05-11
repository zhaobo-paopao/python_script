# 闭包
#   将函数作为返回值返回，也是一种高阶函数
#   这种高阶函数我们也称为叫做【闭包】，通过闭包可以创建一些只有当前函数能访问的变量
#   我们可以将一些私有的数据藏到的闭包中

def fn() :
    a = 10
    # 在函数内部再定义一个函数
    def inner() :
        print('我是fn2', a)

    # 将内部函数 inner 作为返回值返回   
    return inner

r = fn()    
r()
# r 是一个函数，是调用 fn() 后返回的函数，该函数没有参数
#   这个函数是在 fn() 内部定义，并不是全局函数
#   所以这个函数总是能访问到 fn() 函数内的变量，比如：a，而外部不能访问 a。
'''
注意：
    在全局位置不能访问局部位置的变量。
    如果希望在函数内部（局部位置）来修改全局变量，则需要使用 global 关键字，声明在函数内部使用的局部变量是全局变量。
'''

# 求多个数的平均值
# nums = [50, 30, 20, 10, 77]

# sum() 用来求一个列表中所有元素的和
# print(sum(nums)/len(nums))

# 形成闭包的必要条件：
#   ① 有函数嵌套
#   ② 外部函数将内部函数作为返回值返回
#   ③ 内部函数必须要使用到外部函数中的变量，这样闭包才有意义！
def make_averager() :
    # 创建一个列表，用来保存数值
    nums = []

    # 创建一个函数，用来计算平均值
    def averager(n) :
        # 将n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums)/len(nums)

    return averager

averager = make_averager()  # averager 是一个函数，是调用 make_averager() 后返回的函数，该函数有一个参数，即该函数调用时需要传入参数
# print(averager(10))         # 调用 averager 函数：averager(10)
# print(averager(20))
# print(averager(30))
# print(averager(40))

def fn():
    a=10
    def inner():
        print('我是fn2',a)
    return inner
r=fn()
# r()
# 求多个数的平均值
nums=[50,30,20,10,77]
# sum()
# print(sum(nums)/len(nums))
# print(avg())
# def make_averager():
#     nums=[]
#     def averager(n):
#         nums.append(n)
#         return sum(nums)/len(nums)
#     return averager
# averager=make_averager()  #averager 是一个函数，是调用 make_averager() 后返回的函数，该函数有一个参数，即该函数调用时需要传入参数
# print(averager(10))         # 调用 averager 函数：averager(10)
# print(averager(20))
# print(averager(30))
# print(averager(40))

# def make_multipiler(n):
#     def multipiler(x):
#         return x*n
#     return multipiler
# double=make_multipiler(2)
# triple=make_multipiler(3)
# print(double(5))
# print(triple(5))
# def greeting():
#     message='hello'
#     def inner():
#         print(message)
#     message='second'
#     return inner
# f=greeting()
# f()
'''闭包构成条件
   ①:函数嵌套
   ②:内部函数使用外部函数的变量
   ③:外部函数的返回值是内部函数本身,不会随着外部函数调用完而销毁
   
'''
def func_out(num1):
    # 定义一个内部函数
    def func_inner(num2):
        # 内部函数使用外部函数的变量
        '''当前func_inner 函数就是一个闭包函数
            闭包函数的外部函数的返回值是内部函数
            返回的内部函数就是闭包
        '''
        nonlocal num1 #告诉解析器num1使用的是外部变量
        num1=10     # 直接修改外部函数的变量是不行的,得加上nonlocal这个关键字
        result=num1+num2
        print('结果是:',result)
    return func_inner
# 调用外部函数，此时外部函数调用的返回值其实就是func_inner

f=func_out(1)  #用f来接收外部函数的返回值
'''此时打印f  结果入下,其实就是指向的内部函数
'''
print(f)  #<function func_out.<locals>.func_inner at 0x0000022231F1CEA0>
'''此时f等同于func_inner
   此时f()就相当于func_inner()函数的调用
'''
# 执行闭包
f(2)

