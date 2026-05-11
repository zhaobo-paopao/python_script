def sum(*nums):
    total = 0
    for n in nums:
        total += n
    print(total)


# sum(123,456,859)
# return 后边跟什么值，函数就会返回什么值
# return 后边可以跟任意的对象，返回值甚至可以是一个函数
def fn():
    return "hello"

    # return [1,2,3]
    # return {'k':'v'}
    def fn2():
        print("hello")

    return fn2


# r=fn()
# print(r)


# 如果仅仅写一个 return 或者不写 return，则相当于 return None
def fn2():
    a = 10
    return


# print(fn2())
# 在函数中，return 后的代码都不会执行，return 一旦执行，则函数自动结束


def fn3():
    print("hello")
    return
    print("abc")


# print(fn3())


# 生成一个这样的自然数序列：[0, 1, 2, 3, 4]
def fn4():
    for i in range(5):
        if i == 3:
            break  # 用来退出当前循环
        # continue 用来跳过当次循环
        # return 用来结束函数
        print(i)
    print("循环执行完毕")


# fn4()


def sum(*nums):
    # 定义一个变量，来保存结果
    result = 0
    # 遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    return result


r = sum(123, 456, 789)


# print(r+700)
def fn5():
    return 10


print(
    fn5
)  # fn5 是函数对象，打印 fn5 实际是在打印函数对象：<function fn5 at 0x0000023B49104680>
print(fn5())  # fn5() 是在调用函数，打印 fn5() 实际上是在打印 fn5() 函数的返回值：10
