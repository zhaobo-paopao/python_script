file_name='demo.txt'
# with open(file_name,'w',encoding='utf-8') as file_obj: #覆盖原来内容
with open(file_name,'a',encoding='utf-8') as file_obj: #在原来内容上追加

    # write( )来向文件中写入内容
    # 如果操作的是一个文本文件的话，则write()需要传递一个字符串作为参数
    # file_obj.write('hello hello how are you!')
    # 加上'\n'达到换行目的
    file_obj.write('aaa\n')
    file_obj.write('bbb\n')
    file_obj.write('ccc\n')
    r= file_obj.write(str(123)+'123123\n')
    print(r)



