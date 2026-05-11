# 不定长的参数
# 定义一个函数，可以求任意个数字的和
def sum(*nums):
    result = 0
    for n in nums:
        result += n
    print(result)


# sum(123, 456, 789, 10, 20, 30, 40)

# 在定义函数时，可以在形参前边加上一个*，这样这个形参将会获取到所有的实参
# 它将会将所有的实参保存到一个元组中
a, b, *c = (1, 2, 3, 4, 5, 6)  # 元组的解包（解构）


# *a 会接受所有的位置实参，并且会将这些实参统一保存到一个元组中（参数的装包）
def fn(*a):
    print("a=", a, type(a))


# fn(1,2,3,4,5,6)
# 带星号的形参只能有一个
# 带星号的参数，可以和其他参数配合使用
# 第一个参数给 a，第二个参数给 b，剩下的都保存到 c 的元组中
# def fn2(a,b,*c):
#     print('a=',a)
#     print('b=',b)
#     print('c=',c)
# fn2(1,2,3,4,5)
# 可变参数不是必须写在最后，但是注意，带*的参数后的所有参数，必须以关键字参数的形式传递
# 第一个参数给 a，剩下的位置参数给 b 的元组，c 必须使用关键字参数
# def fn2(a, *b, c) :
#     print('a =', a)   # a = 1
#     print('b =', b)   # b = (2, 3, 4)
#     print('c =', c)   # c = 5
# fn2(1, 2, 3, 4, c=5)
# def fn2(*a,b,c):
#     print('a =', a)   # a = 1
#     print('b =', b)   # b = (2, 3, 4)
#     print('c =', c)   # c = 5
# fn2(1,2,3,b=4,c=5)


# 如果在形参的开头直接写一个*，则要求我们的所有的参数必须以关键字参数的形式传递
# def fn2(*,a,b,c):
#     print('a =', a)   # a = 1
#     print('b =', b)   # b = (2, 3, 4)
#     print('c =', c)   # c = 5
# fn2(a=3,b=4,c=5)
# *形参只能接收位置参数，而不能接收关键字参数
# def fn3(*a) :
#     print('a =', a)   # a = (1, 2, 3, 4, 5)
# fn3(1,2,3,4,5)
# **形参可以接收其他的关键字参数，它会将这些参数统一保存到一个字典中
#   字典的 key 就是参数的名字，字典的 value 就是参数的值
# **形参只能有一个，并且必须写在所有参数的最后
# def fn3(b, c, **a) :
#     print('a =', a, type(a))    # a = {'d': 2, 'e': 10, 'f': 20} <class 'dict'>
#     print('b =', b)     # b = 1
#     print('c =', c)     # c = 3
# fn3(b=1,d=2,c=3,e=10,f=20)
# 参数的解包（拆包）
def fn4(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)


# 创建一个元组
# t = (10, 20, 30)
# 创建一个列表
t = [10, 20, 30]
# fn4(*t)
# 传递实参时，也可以在序列类型的参数前添加星号，这样它会自动将序列中的元素依次作为参数传递
# 这里要求序列中元素的个数必须和形参的个数的一致
# fn4(t[0], t[1], t[2])     # 此种方式太麻烦了
d = {"a": "100", "b": "200", "c": "300"}
# fn4(**d)


# def func(*args):
#     print(f'args的类型为:{type(args)}')
#     print(f'args的值为:{args}')
#     print(f'args的长度为:{len(args)}')
#     for i,arg in enumerate(args):
#        print(f'参数{i}:{arg}')
# func(1,2,3,4,5)
# 实际应用：求和函数
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)


# sum_all(1,2,3)
# sum_all(1,2,3,4,5,6)
# sum_all()
# **kwargs- 可变关键字参数
def func(**kwargs):
    print(f"kwargs的类型为:{type(kwargs)}")
    print(f"kwargs的值为:{kwargs}")
    print(f"kwargs的长度为:{len(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key} = {value}")


# func(name='张三',age=25,city='北京')
#  参数解包（Unpacking）
def func(a, b, c):
    print(f"a={a},b={b},c={c}")


numbers = (1, 2, 3)
# func(*numbers)


def func(name, age, gender):
    print(f"name={name},age={age},gender={gender}")
    # print('name= ',name)
    # print('age= ',age)
    # print('gender= ',gender)


dicts = {"name": "张三", "age": 23, "gender": "male"}
# func(**dicts)
