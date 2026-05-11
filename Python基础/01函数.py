# 定义一个函数
'''def fn():
    print('这是我的第一个函数')
    print('hrllo')
    print('鄂温克人')

def fn2(a,b,c): 
    print(a+b+c)
# fn2(10,20,30)
def fn3(a,b,c):
  result=a*b*c
  print(result)
fn3(1,5,6)'''

def sum(*nums):
    result=0
    for n in nums:
        result+=n
    return result
r=sum(123,456,789)
print(r)


def fn5():
    return 10
print(fn5)
print(fn5())