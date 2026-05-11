# 普通函数 - 一次性返回所有结果
def normal_func():
    result=[]
    for i in range(3):
        result.append(i)
    return result
# print(normal_func())  # 一次性返回 [0, 1, 2]

# 生成器函数 - 逐个生成结果
def generator_func():
    for i in range(3):
        yield i   # 每次产生一个值
gen=generator_func()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for value in gen:
    pass
    # print("遍历生成器得到的值：",value)

def simple_generator():
    print('开始执行')
    yield 1
    print('继续执行')
    yield 2
    print('结束执行')
    yield 3
# 创建生成器对象
gen=simple_generator()
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fibonacci()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

def magic_generator():
    yield 1
    yield 2
    yield 3

gen = magic_generator()
# print(next(gen))
def f1():
    p=[1,2,3,4]
    s=map(lambda x: x*2,p)
    print(list(s))
f1()


