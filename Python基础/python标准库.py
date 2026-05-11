# 开箱即用
# 为了实现开箱即用的思想,Python中为我们提供了一个模块的标准库午这个标准库中,
# 有很多很强大的模块我们可以直接使用,并且标准库会随Python的安装一同安装5ys模块,
# 它里面提供了一些变量和函数,使我们可以获取到Python解析器的信息或者通过函数来操作Python解析器引入sys模块
import sys
# print(sys)
# 获取执行代码时，命令行中所包含的参数该属性是一个列表，列表中保存了当前命令的所有参数
import pprint
sys.path
# print(sys.argv)
# # sys.modules
sys.platform
import os
# sys.exit('程序出现异常结束........')
os.environ
# pprint.pprint(sys.modules)
# pprint.pprint(sys.path)
# print(sys.platform)
# print (os)
# print (os.environ)
os.system('dir')
os.system('notepad')

pprint.pprint(os.environ['path'])
