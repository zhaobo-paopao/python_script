print('异常出现前')
l=[]
try:
    # print(c)
    1+'hello'
    l[10]
    print(10/0)
except NameError:
    print('异常 NameError 出现的代码....')
except ZeroDivisionError:
    print('异常 ZeroDivisionError 出现的代码....')
except IndexError:
    print('异常 IndexError 出现的代码....')
except Exception as e:
    print('未知异常',e,type(e))
finally:
    print('无论出现什么异常,该子句都会执行')
print('异常出现后')