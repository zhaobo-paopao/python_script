'''
try 语句
    try:
        代码块(可能出错的语句)
    except:
        代码块(出现错误以后的处理方式)
    else:
        代码块(没出错时要执行的语句)
'''

# print('hello')
# try:
#     print(10/3)
# except:
#     print('哈哈哈,出错了....')
# else:
#     print('程序正常执行....')
# print('你好')

# print(10/0)
def fn():
    print('hello fn')
    print(10/0)
def fn2():
    print('hello fn2')
    fn()
def fn3():
    print('hello fn3')
    fn2()
fn3()
