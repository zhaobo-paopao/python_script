# 创建一个程序打印如下图形
# *****
# *****
# *****
# *****
# *****
'''i=0
while i<5:
    j=0
    while j<5:
         print('* ',end='')
         j+=1
    print()
    i+=1'''
# 创建一个程序打印如下图形
# *
# **
# ***
# ****
# *****
'''i=0
while i<5:
    j=0
    while j<i+1:
         print('* ',end='')
         j+=1
    print()
    i+=1'''
# 创建一个程序打印如下图形
# *****
# ****
# ***
# **
# *
i=0
while i<5:
    j=0
    while j<5-i:
         print('* ',end='')
         j+=1
    print()
    i+=1