# 员工管理系统
# 使用Python基本语法实现

def show_welcome():
    """显示欢迎界面"""
    print("=" * 50)
    print(" " * 15 + "欢迎使用员工管理系统")
    print("=" * 50)
    print()
    print("系统功能：")
    print("1. 添加新员工")
    print("2. 查看所有员工")
    print("3. 搜索员工")
    print("4. 删除员工")
    print("5. 修改员工信息")
    print("6. 退出系统")
    print()

def add_employee(employees):
    """添加新员工"""
    print("\n--- 添加新员工 ---")
    
    while True:
        try:
            emp_id = int(input("请输入员工ID: "))
            # 检查ID是否已存在
            for emp in employees:
                if emp["id"] == emp_id:
                    print("错误：员工ID已存在，请重新输入！")
                    break
            else:
                break
        except ValueError:
            print("错误：请输入有效的数字ID！")
    
    name = input("请输入员工姓名: ")
    
    while True:
        try:
            age = int(input("请输入员工年龄: "))
            if age < 18 or age > 65:
                print("年龄应在18-65之间，请重新输入！")
            else:
                break
        except ValueError:
            print("错误：请输入有效的年龄数字！")
    
    department = input("请输入员工部门: ")
    
    while True:
        try:
            salary = float(input("请输入员工工资: "))
            if salary < 0:
                print("工资不能为负数，请重新输入！")
            else:
                break
        except ValueError:
            print("错误：请输入有效的工资数字！")
    
    # 创建员工字典
    employee = {
        "id": emp_id,
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    
    # 添加到员工列表
    employees.append(employee)
    print(f"员工 {name} 添加成功！")
    return employees

def show_all_employees(employees):
    """显示所有员工"""
    print("\n--- 所有员工信息 ---")
    
    if not employees:
        print("目前没有员工信息。")
        return
    
    # 表头
    print(f"{'ID':<8} {'姓名':<10} {'年龄':<6} {'部门':<12} {'工资':<10}")
    print("-" * 50)
    
    # 员工信息
    for emp in employees:
        print(f"{emp['id']:<8} {emp['name']:<10} {emp['age']:<6} {emp['department']:<12} ￥{emp['salary']:<8.2f}")
    
    print(f"\n总计: {len(employees)} 名员工")

def search_employee(employees):
    """搜索员工"""
    print("\n--- 搜索员工 ---")
    
    if not employees:
        print("目前没有员工信息。")
        return
    
    print("搜索方式:")
    print("1. 按员工ID搜索")
    print("2. 按员工姓名搜索")
    print("3. 按部门搜索")
    
    choice = input("请选择搜索方式 (1-3): ")
    
    if choice == "1":
        try:
            search_id = int(input("请输入要搜索的员工ID: "))
            found = False
            for emp in employees:
                if emp["id"] == search_id:
                    print("\n找到员工:")
                    print(f"ID: {emp['id']}")
                    print(f"姓名: {emp['name']}")
                    print(f"年龄: {emp['age']}")
                    print(f"部门: {emp['department']}")
                    print(f"工资: ￥{emp['salary']:.2f}")
                    found = True
                    break
            if not found:
                print(f"未找到ID为 {search_id} 的员工。")
        except ValueError:
            print("错误：请输入有效的数字ID！")
    
    elif choice == "2":
        search_name = input("请输入要搜索的员工姓名: ")
        results = [emp for emp in employees if search_name.lower() in emp["name"].lower()]
        
        if results:
            print(f"\n找到 {len(results)} 个匹配的员工:")
            for emp in results:
                print(f"ID: {emp['id']}, 姓名: {emp['name']}, 部门: {emp['department']}, 工资: ￥{emp['salary']:.2f}")
        else:
            print(f"未找到姓名为 '{search_name}' 的员工。")
    
    elif choice == "3":
        search_dept = input("请输入要搜索的部门: ")
        results = [emp for emp in employees if search_dept.lower() in emp["department"].lower()]
        
        if results:
            print(f"\n部门 '{search_dept}' 共有 {len(results)} 个员工:")
            for emp in results:
                print(f"ID: {emp['id']}, 姓名: {emp['name']}, 年龄: {emp['age']}, 工资: ￥{emp['salary']:.2f}")
        else:
            print(f"未找到部门为 '{search_dept}' 的员工。")
    
    else:
        print("无效的选择！")

def delete_employee(employees):
    """删除员工"""
    print("\n--- 删除员工 ---")
    
    if not employees:
        print("目前没有员工信息。")
        return employees
    
    show_all_employees(employees)
    
    try:
        delete_id = int(input("\n请输入要删除的员工ID: "))
        
        for i, emp in enumerate(employees):
            if emp["id"] == delete_id:
                name = emp["name"]
                del employees[i]
                print(f"员工 {name} (ID: {delete_id}) 已删除。")
                return employees
        
        print(f"未找到ID为 {delete_id} 的员工。")
    
    except ValueError:
        print("错误：请输入有效的数字ID！")
    
    return employees

def update_employee(employees):
    """修改员工信息"""
    print("\n--- 修改员工信息 ---")
    
    if not employees:
        print("目前没有员工信息。")
        return employees
    
    show_all_employees(employees)
    
    try:
        update_id = int(input("\n请输入要修改的员工ID: "))
        
        for i, emp in enumerate(employees):
            if emp["id"] == update_id:
                print(f"\n当前员工信息:")
                print(f"1. 姓名: {emp['name']}")
                print(f"2. 年龄: {emp['age']}")
                print(f"3. 部门: {emp['department']}")
                print(f"4. 工资: ￥{emp['salary']:.2f}")
                
                field = input("\n请输入要修改的项目 (1-4, 输入0取消): ")
                
                if field == "0":
                    print("修改已取消。")
                    return employees
                
                elif field == "1":
                    new_name = input("请输入新的姓名: ")
                    employees[i]["name"] = new_name
                    print("姓名已更新。")
                
                elif field == "2":
                    while True:
                        try:
                            new_age = int(input("请输入新的年龄: "))
                            if 18 <= new_age <= 65:
                                employees[i]["age"] = new_age
                                print("年龄已更新。")
                                break
                            else:
                                print("年龄应在18-65之间，请重新输入！")
                        except ValueError:
                            print("错误：请输入有效的年龄数字！")
                
                elif field == "3":
                    new_dept = input("请输入新的部门: ")
                    employees[i]["department"] = new_dept
                    print("部门已更新。")
                
                elif field == "4":
                    while True:
                        try:
                            new_salary = float(input("请输入新的工资: "))
                            if new_salary >= 0:
                                employees[i]["salary"] = new_salary
                                print("工资已更新。")
                                break
                            else:
                                print("工资不能为负数，请重新输入！")
                        except ValueError:
                            print("错误：请输入有效的工资数字！")
                
                else:
                    print("无效的选择，修改已取消。")
                
                return employees
        
        print(f"未找到ID为 {update_id} 的员工。")
    
    except ValueError:
        print("错误：请输入有效的数字ID！")
    
    return employees

def save_to_file(employees, filename="employees.txt"):
    """保存员工信息到文件"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for emp in employees:
                f.write(f"{emp['id']},{emp['name']},{emp['age']},{emp['department']},{emp['salary']}\n")
        print(f"员工信息已保存到 {filename}")
    except Exception as e:
        print(f"保存文件时出错: {e}")

def load_from_file(filename="employees.txt"):
    """从文件加载员工信息"""
    employees = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 5:
                    employee = {
                        "id": int(data[0]),
                        "name": data[1],
                        "age": int(data[2]),
                        "department": data[3],
                        "salary": float(data[4])
                    }
                    employees.append(employee)
        print(f"从 {filename} 加载了 {len(employees)} 名员工信息")
    except FileNotFoundError:
        print("未找到保存文件，将使用空的员工列表")
    except Exception as e:
        print(f"加载文件时出错: {e}")
    
    return employees

def main():
    """主函数"""
    # 员工列表
    employees = []
    
    # 从文件加载员工信息
    employees = load_from_file()
    
    while True:
        # 显示欢迎界面
        show_welcome()
        
        # 获取用户选择
        choice = input("请选择功能 (1-6): ")
        
        if choice == "1":
            employees = add_employee(employees)
        elif choice == "2":
            show_all_employees(employees)
        elif choice == "3":
            search_employee(employees)
        elif choice == "4":
            employees = delete_employee(employees)
        elif choice == "5":
            employees = update_employee(employees)
        elif choice == "6":
            # 退出前保存数据
            save_choice = input("是否保存员工信息到文件? (y/n): ").lower()
            if save_choice == "y":
                save_to_file(employees)
            print("感谢使用员工管理系统，再见！")
            break
        else:
            print("无效选择，请重新输入！")
        
        # 暂停一下，让用户看到结果
        input("\n按回车键继续...")

# 程序入口
if __name__ == "__main__":
    main()