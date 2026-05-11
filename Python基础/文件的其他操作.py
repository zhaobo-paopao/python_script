import os
import shutil
from pprint import pprint
r=os.listdir('..')
r=os.getcwd()
# os.chdir('c:/')
# r=os.getcwd()
# os.mkdir('大结局')
# os.rmdir('大结局')
# open('111.txt','w')
# os.remove('111.txt')
# os.rename('111.txt','222.txt')
# os.rename('222.txt','c:/Users/60403/Desktop/222.txt')
shutil.move('222.txt','c:/Users/60403/Desktop/222.txt')

pprint(r)