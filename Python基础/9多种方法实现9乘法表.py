# # 第一种 while-while循环
i=1
# while i<=9:
#     j=1
#     while j<i+1:
#      print(f"{j}*{i}={i*j} ",end='')
#      j+=1
#     i+=1
#     print()
# # 第二种 while-while循环(i的初始值不同)
# i=0
# while i<9:
#     i+=1
#     j=1
#     while j<i+1:
#      print(f"{j}*{i}={i*j} ",end='')
#      j+=1
#     print()
# # 第三种 for-for循环
# for i in range(1,10):
#  for j in range(1,i+1):
#    print(f"{j}*{i}={i*j} ",end='')
#  print()
# # 第四种 while-for循环
i=0
# while i<9:
#   i+=1
#   for j in range(1,i+1):
#     print(f"{j}*{i}={i*j} ",end='')
#   print()
# # 第五种 for -while循环
# for i in range(1,10):
#   j=0
#   while j<i:
#        j+=1
#        print(f"{j}*{i}={i*j} ",end='')
#   print()
# # 第六种 自定义列表变量配合for循环
# a=[1,2,3,4,5,6,7,8,9] 
# for i in a:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={i*j} ",end='')
#         j+=1
#     print()
# # 第七种 使用递归函数
def multiplication(n):
	if n < 10:
		for m in range(1, n+1):
			print(f"{m}*{n}={m*n} ", end="")
		print()
		multiplication(n+1)
multiplication(1)





 

