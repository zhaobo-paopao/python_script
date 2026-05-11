# 显示系统的欢迎界面
print('-'*30,'欢迎使用员工管理系统','-'*30)
# 创建一个列表保存员工信息
emps=['小明\t18\t男\t西安','小李\t20\t男\t宝鸡','小王\t23\t女\t榆林','小赵\t40\t女\t渭南']
# 创建一个死循环,反复显示这些提示信息
while True:
    # 显示用户的选项
    print('请选择您需要的操作:')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    user_choose=int(input('请选择[1-4]'))
    # 根据用户的选择做相关的操作
    if user_choose==1:  
       #查询员工
       #打印表头
       print('\t序号\t姓名\t年龄\t性别\t住址')
    #    创建一个变量来表示员工的序号
       n=1
    #    显示员工信息
       for emp in emps:
          print(f'\t{n}\t{emp}')
          n+=1

    #  pass
    elif user_choose==2:   
        #添加员工
        # 获取要添加员工的信息,姓名，年龄,性别，地址
        emp_name=input('请输入员工的姓名:')
        emp_age=input('请输入员工的年龄:')
        emp_sex=input('请输入员工的性别:')
        emp_address=input('请输入员工的地址:')
        # 创建员工信息
        emp = f'{emp_name}\t{emp_age}\t{emp_sex}\t{emp_address}'
          # 显示提示信息
        print('以下员工将会被添加到系统中')
        print('-'*62)
        print('\t姓名\t年龄\t性别\t地址')
        print(f'\t{emp}')
        print('-'*62)

  # 确认信息
        user_confirm = input('是否确认该操作[Y/N]:')
        if user_confirm == 'y' or user_confirm == 'Y' or user_confirm == 'yes' :
            # 拼接字符串，插入列表中
            emps.append(emp)
            print('插入员工成功！')
        else :
            print('插入员工已取消！')
    elif user_choose==3:  #删除员工  
    #  删除员工，根据员工的序号删除
    # 获取要删除员工的序号
        del_num=int(input('请输入要删除员工的序号:'))
    # 判断序号是否有效
        if  0<=del_num<=len(emps):
        #    输入合法,根据序号获取索引
             del_i=del_num-1
            #  显示提示信息
             print("以下员工信息将被删除")
             print("-"*60)
             print("\t序号\t姓名\t年龄\t性别\t住址")
             print(f'\t{del_num}\t{emps[del_i]}')
             user_confirm=input('该操作不可恢复,请确认[Y/N]:')
             if user_confirm == 'y' or user_confirm == 'Y' or user_confirm == 'yes' :
                # 拼接字符串，插入列表中
                emps.pop(del_i)
                print('删除员工成功！')
             else:
                print('删除员工已取消！')
        else:
            print('您的输入有误，请重新操作！')
    elif user_choose==4:
    #  退出
        print('欢迎使用员工管理系统!再见！')
        input('点击回车键退出！')
        break
    
    else:
        print('您的输入有误,请重新输入!')
    print('-'*60)


