#可以自定义异常类,只需要一个类来继承Exception
class MyError(Exception):
    pass
def add(a,b):
    # 如果a和b中有负数,就向调用处抛出异常
    if a<0 or b<0:
        # raise Exception('两个参数中不能有负数')
        # return None
        raise MyError('这是我自定义的错误')
    r=a+b
    return r
print(add(-123,456))