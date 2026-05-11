#打印欢迎界面 Empolyee_Manager_System:员工管理系统
print("-"*35,"欢迎使用员工管理系统","-"*35)
#定义员工列表并添加四个元素
emps=['小明\t15\t男\t西安市','小李\t20\t女\t延安市','小张\t25\t男\t北京市','小王\t26\t女\t上海市']
while True:
    print("请选择您要做的操作:")
    print("\t1.查询员工")    #"\t"为缩进占位符 查询当前系统中所有的员工
    print("\t2.添加员工")    #将员工添加到系统中
    print("\t3.删除员工")    #将员工从系统中删除
    print("\t4.退出系统")    #退出系统
    user_choose=input("请选择您要做的操作[1-4]:")
    #1.查询员工信息
    if user_choose=='1':    
        #打印表头字段信息
        print("\t序号\t姓名\t年龄\t性别\t住址")
        n=1 #定义序号n,动态生产
        #for循环输出列表元素
        for emp in emps:
            #拼接序号和员工列表,动态生产序号
            print(f"\t{n}\t{emp}")  
            n+=1
        pass
    #2.添加员工信息
    elif user_choose=='2':
        user_name=input("请输入员工姓名:")
        ser_age=input("请输入员工年龄:")
        ser_sex=input("请输入员工性别:")
        ser_addrss=input("请输入员工地址:")
        #向员工列表中添加一个员工信息,定义emp变量保存接收到的员工信息
        emp=(f"{user_name}\t{ser_age}\t{ser_sex}\t{ser_addrss}")
        print("以下员工信息将添加到系统中!!!!!!!!!")
        print("-"*70)
        print("姓名\t年龄\t性别\t住址")
        print(emp)
        user_confirm=input("是否添加？(Y/N):")
        #判断
        if user_confirm=='y' or user_confirm=='yes':
            emps.append(emp)
            #显示提示信息
            print("添加成功!")
        else:
            #取消操作,添加失败
            print("添加失败!")
        #3.删除员工信息
    elif user_choose=='3':
        #获取要删除员工的序号
        #del_num为用户输入的员工序号,但是实际删除时,我们用的是列表的索引，所以用emp_no保存索引的值
        emp_no=int(input("请输入要删除的员工的序号："))
        #判断序号是否合法
        if 0<emp_no<=len(emps):  #员工序号必须小于等于列表长度
            emp_index=emp_no-1
            #显示一个提示信息
            print("以下员工将被删除")
            print("\t序号\t姓名\t年龄\t性别\t住址")
            print(f"\t{emp_no}\t{emps[emp_index]}") #输出的表内容根据员工的序号和员工的索引值拼接输出
            user_confirm=input("该操作不可恢复,请确认是否删除(Y/N:")
            #判断
            if user_confirm=='y' or user_confirm=='yes':
              #删除元素
                emps.pop(emp_index)
              #显示提示
                print("员工已被删除!")
            else:
                print("操作已经取消!")
        else:
            print("您输入的员工序号有误!,请重新输入!")
    elif user_choose=='4':
        #退出
        print("感谢使用,再见!")
        exit()
    else:
        print("您的输入有误,请重新输入!")
