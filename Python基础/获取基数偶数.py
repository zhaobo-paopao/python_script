# 编写一个程序获取用户输入的数字,通过程序显示这个数字是基数还是偶数
num=int(input("请输入一个整数:"))
if num %2==0:
    print(num,'这个数字是偶数')
else:
    print(num,"这个数字是基数")
