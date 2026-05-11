file_name='c:/Users/60403/Desktop/BGM2.MP3'
# 读取模式
# t 默认读取文本
# b 读取二进制
with open (file_name,'rb') as file_obj:
    # 读取文本文件时，size是以字符为单位的
    # 读取二进制文件时，size是以字节为单位
    print(file_obj.read(100))
    # 把读到的内容写进去
    # 定义一个文件
    new_name='aa.mp3'
    with open(new_name,'wb') as new_obj:
        # 定义每次读出来的大小
        chunk=1024*100
        while True:
            # 从已有的对象中读取数据
            content=file_obj.read(chunk)
            # 内容读取完毕,终止循环
            if not content:
                break
            # 将读到的内容写到新对象中
            new_obj.write(content)



