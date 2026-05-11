import os
import sys
from  kafka import KafkaProducer
current_dir=os.path.dirname(os.path.abspath(__file__))  #定位当前脚本的位置路径，作为路径计算的起点
# e:\workspace\python_script\python基础练习\相对路径和绝对路径.py
 #返截取路径的「目录部分」，去掉文件名
project_root=os.path.dirname(current_dir)
# e:\workspace\python_script\python基础练习
# current_dir1=os.pardir
# current_dir2=os.path.defpath()
# print(current_dir2)
# print(current_dir1)
if project_root  not in sys.path:
    sys.path.insert(0,project_root)
print(current_dir)
print(project_root)


