# print('这是一个module')
# print(__name__)
a=2
b=1
# 添加了_的变量，只能在模块内部访问，在通过import *引入时,不会引入_开头的变量
_c=30
def test():
    print('test')
def test2():
    print('test2')
class Person:
    def __init__(self) -> None:
        self.name='孙悟空'
#编写测试代码，这部分代码，只要当当前文件作为主模块的时候才需要执行而当模块被其他模块引入时，
#不需要执行的，此时我们就必须要检查当前模块是否是主模块
if __name__=='__main__':
    test()
    test2()
    p=Person()
    print(p.name)