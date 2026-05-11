# file_name='demo.txt'
# file_obj=open(file_name)
# content=file_obj.read()
# print(content)
# file_obj.close()
# # 关闭  
# # file_obj.close()  
# # file_obj.read()

# with  open(file_name)as file_obj:
#     print(file_obj.read())
# file_obj.read()
file_name='demo.txt'
try:
    with  open(file_name)as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name}文件不存在----')

