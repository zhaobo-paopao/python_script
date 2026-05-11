# 显示提示信息
print("*" * 40, "欢迎光临孙悟空大战白骨精游戏!", "*" * 40)  # 语句左右打印40个*作为分隔符
print("请选择你的身份：")
print("\t1. 孙悟空")
print("\t2. 白骨精")
# 游戏身份选择,根据用户选择来分配身份
player_choose = input("请选择你的角色身份[1-2]:")  # input输出结果为字符串

# 打印分隔符字符串
print("*" * 112)

# 根据用户输入的信息选择角色
if player_choose == '1':  # 选择孙悟空
    print("您选择的角色是孙悟空,您将以孙悟空的角色来进行本次游戏!")
elif player_choose == '2':  # 选择白骨精
    print("您选择的角色是白骨精,您将以白骨精的角色来进行本次游戏!")
else:
    print("您输入的角色信息不合法,请重新输入!")
    exit()  # 如果输入不合法，退出程序

# 游戏进行部分
if player_choose == '1':
    # 孙悟空的初始属性
    attack = 10
    health = 100
elif player_choose == '2':
    # 白骨精的初始属性
    attack = 8
    health = 120

print(f"您的角色是{player_choose}，攻击力：{attack}，生命值：{health}")

while True:
    print("\n请选择您可以进行的操作：")
    print("1. 练级")
    print("2. 打 BOSS")
    print("3. 逃跑")
    action = input("请输入操作编号[1-3]: ")

    if action == '1':
        # 练级
        attack += 2
        health += 5
        print(f"练级成功！攻击力提升到{attack}，生命值提升到{health}。")
    elif action == '2':
        # 打 BOSS
        boss_attack = 15
        boss_health = 150
        while True:
            # 玩家攻击BOSS
            boss_health -= attack
            print(f"玩家攻击BOSS，BOSS生命值剩余{boss_health}。")
            if boss_health <= 0:
                print("恭喜你，打败了BOSS！游戏胜利！")
                break

            # BOSS反击玩家
            health -= boss_attack
            print(f"BOSS反击玩家，玩家生命值剩余{health}。")
            if health <= 0:
                print("很遗憾，你被BOSS打败了。游戏结束！")
                break
    elif action == '3':
        # 逃跑
        print("你选择了逃跑，游戏结束！")
        break
    else:
        print("无效的操作，请重新输入！")