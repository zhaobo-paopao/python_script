enumerate() 函数是一个内置函数,用于在迭代过程中同时获取元素的索引和值。它返回一个枚举对象,包含了索引和对应的元素。
函数基本、用法
enumerate(iterable,start=0)
参数说明:
iterable:必需,一个可迭代对象,如列表、元组、字符串等。
start:可选,指定索引的起始值,默认为 0。
1:基本用法
fruits=['apple','banana','orange','grape','mango','cherry']  #cherry樱桃
for index,fruit in enumerate(fruits): 
    print(index,fruit)
2:指定索引起始值为1
fruits=['apple','banana','orange','grape','mango','cherry']  #cherry樱桃
for index,fruit in enumerate(fruits,start=1):  #定索引的起始值为1
    print(index,fruit)
3:指定索引起始值为2
fruits=['apple','banana','orange','grape','mango','cherry']  #cherry樱桃
for index,fruit in enumerate(fruits,start=2):  #定索引的起始值为2
    print(index,fruit)
4:序列解包(Unpacking)
解包(Unpacking)是Python中一种非常强大且灵活的特性,它允许我们将序列(如列表、元组)或映射(如字典)中的元素分解为单独的变量。解包可以大大简化代码,使其更加简洁和易读。
fruits=['apple','banana','orange','grape','mango','cherry']  #cherry樱桃
for index, _ in enumerate(fruits):   
 print(index)
在上述情况下,可以使用下划线 _ 来表示不需要的值,以减少内存消耗。
5:枚举对象转换为列表或者元组
fruits=['apple','banana','orange','grape','mango','cherry']  #cherry樱桃
en_list=list(enumerate(fruits))
en_tuple=tuple(enumerate(fruits))
print(en_list)
print(en_tuple)

可以使用 list() 或 tuple() 函数将枚举对象转换为列表或元组。

上述是 enumerate() 函数的一些常见用法。

当使用enumerate()函数时,还可以结合其他常用的Python函数和技巧来实现更多功能。
6:反向遍历列表和索引
fruits=['apple','banana','orange','grape','mango','cherry']  #cherry樱桃
for index,fruit in enumerate(reversed(fruits)):
  print(index,fruit)
  通过使用reversed()函数,可以反向遍历列表并获取相应的索引和值。
7:枚举多个可迭代对象
fruits=['apple','banana','orange','grape','mango','cherry']  #cherry樱桃
prices=[2.5,3.0,2.3,6.8,11.2,40.5]
for index,(fruit,price) in enumerate(zip(fruits,prices)):
  print(index,fruit,price)
上面例子中,我们使用了zip()函数将多个可迭代对象(fruits和prices)进行组合,并使用enumerate()获取索引和对应的值。
8:枚举字典的键值对
import items 
fruits={'apple':2.5,'banana':3.0,'orange':2.3,'grape':6.8,'mango':11.2,'cherry':40.5} #cherry樱桃
for index,(fruit,price) in enumerate (fruits.items()):
   print(index,fruit,price)
   通过使用items()方法，可以将字典的键值对转换为可迭代对象，并使用enumerate()获取索引和对应的键值对。
以上便是enumerate()函数的常用方法,希望大家一起交流学习