# file_name='demo2.txt'
# try:
    # 调用open()来打开一个文件，可以将文件分成两种类型一种，
    # 是纯文本文件(使用utf-8等编码编写的文本文件)一种，
    # 是二进制文件(图片、mp3、ppt等这些文件)open()打开文件时，默认是以文本文件的形式打开的，
    # 但是open()默认的编码为None所以处理文本文件时，必须要指定文件的编码
    # with open(file_name,encoding='UTF-8') as file_obj:
    #通过read读取文件中的内容
    # 如果直接调用read()它会将文本文件的所有内容全部都读取出来如果要读取的文件较大的话，
    # 会一次性将文件的内容加载到内存中，
    # 容易导致内存泄漏所以对于较大的文件，不要直接调用read()
    # read()可以接收一个size作为参数,该参数用来指定要读取的字符的数量默认值为-1，
    # 它会读取文件中的所有字符
    # 可以为size指定一个值，这样read()会读取指定数量的字符
    # 每一次读取都是从上次读取到位置开始读取的如果字符的数量小于size，
    # 则会读取剩余所有的如果已经读取到了文件的最后了，则会返回空串
    #  content=file_obj.read(-1)
#      content=file_obj.read(6)
#      content=file_obj.read(6)
#      content=file_obj.read(6)
#      content=file_obj.read(6)
#      content=file_obj.read(6)
#      content=file_obj.read(6)
#      print(content)
#      print(len(content))
# except FileNotFoundError:
#     print(f'{file_name}不存在')

#读取大文件的方式
file_name='demo2.txt'
try:
    with open(file_name,encoding='UTF-8') as file_obj:
        file_content=''
        chunk=100
    while True:
     content=file_obj.read(chunk)
     if not content:
        break
     file_content+=content
    #  print(content)
    #  print(len(content))
except FileNotFoundError:
    print(f'{file_name}不存在')
print(file_content)