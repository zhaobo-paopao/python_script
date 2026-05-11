# 1. 定义装饰器函数
def simple_decorator(func):  # func 参数将接收被装饰的函数
    # 2. 定义内部包装函数
    def wrapper():
        print('函数执行前...') # 添加的新功能
        func() # 调用原始函数
        print('函数执行后...') # 添加的新功能
    return wrapper            # 返回包装函数
 # 3. 使用装饰器语法
@simple_decorator
def say_hello():
    print('hello')
# 4. 调用装饰后的函数
say_hello()
'''
发生了什么：
先定义原函数 say_hello_original（内部打印 "Hello!"）
调用 simple_decorator(say_hello_original)，传入原函数
simple_decorator返回新的 wrapper函数
将 say_hello变量指向这个 wrapper函数
执行顺序:
1. 进入 wrapper() 函数
2. 执行 print("函数执行前...")
3. 调用 func()，即原 say_hello()，打印 "Hello!"
4. 执行 print("函数执行后...")
'''
print('--'*50)

import time # 导入时间模块
# 1. 定义装饰器函数
def timer_decorator(func):  # func 参数接收被装饰的函数
    # 2. 定义包装函数
    def wrapper(*args,**kwargs): # 接收任意数量和类型的参数
    # *args: 接收位置参数元组，如 (1, 2, 3)
    # **kwargs: 接收关键字参数字典，如 {'x': 1, 'y': 2}
        start_time=time.time()  # 记录开始时间
        result=func(*args,**kwargs)  # 调用原函数并传入参数
        end_time=time.time()  # 记录结束时间
        print(f'函数{func.__name__}执行耗时:{end_time-start_time:.4f}秒')
        return result  # 返回原函数的执行结果
    return wrapper   # 返回包装函数
# 3. 使用装饰器
@timer_decorator
def slow_founction(seconds):
    # 模拟耗时操作
    time.sleep(seconds)
    return f'睡了{seconds}秒'  # 让程序暂停 seconds 秒
# 4. 测试调用
print(slow_founction(2))