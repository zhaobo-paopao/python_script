# import items 
# fruits={'apple':2.5,'banana':3.0,'orange':2.3,'grape':6.8,'mango':11.2,'cherry':40.5} #cherry樱桃
# for index,(fruit,price) in enumerate (fruits.items()):
#    print(index,fruit,price)

   
# high=float(input("身高是:"))
# money=float(input("存款是:"))
# shuai=float(input("帅力值是:"))

# 1、身份选择
#     ① 显示提示信息
#         欢迎光临 xxx 游戏！
#         请选择你的身份：
#             1.xxx
#             2.xxx
#         请选择：x
#     ② 根据用户选择来分配身份（显示不同的提示消息）  
#         1.---
#         2.---
#         3.---  

# 2、游戏进行
#     ① 显示玩家的基本信息（攻击力 生命值）
#     ② 显示玩家可以进行的操作：
#         1、练级
#             - 提升玩家的攻击力和生命值
#         2、打 BOSS
#             - 玩家对 BOSS 进行攻击，玩家要攻击 BOSS，BOSS 对玩家进行反击
#             - 计算 BOSS 是否被玩家消灭，玩家是否被 BOSS 消灭
#             - 游戏结束
#         3、逃跑
#             - 退出游戏，显示提示信息，游戏结束！

#显示提示信息
print("*"*40,"欢迎光临孙悟空大战白骨精游戏!","*"*40)  #语句左右打印40个*作为分隔符
print("请选择你的身份：")
print("\t请选择你的身份1.孙悟空")         #'\t'为打印缩进字符串
print("\t请选择你的身份2.白骨精")         #'\t'为打印缩进字符串
#游戏身份选择,根据用户选择来分配身份
player_choose=input("请选择你的角色身份[1-2]:")    #input输出结果为字符串
#打印分隔符字符串
print("*"*112) 
#根据用户输入的信息选择角色
if player_choose=='1':   #选择孙悟空
    print("您选择的角色是孙悟空,您将以孙悟空的角色来进行本次游戏!")
elif  player_choose=='2':  #选择白骨精
    print("您选择的决定是白骨精,您不能大战自己!")
else:
    print("您输入的角色信息不合法,请重新输入!")
  
