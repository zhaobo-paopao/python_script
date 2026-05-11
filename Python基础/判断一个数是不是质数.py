def is_prime(num):
    """
    判断一个数是否为质数
    参数:
        num: 待判断的整数
    返回:
        bool: 是质数返回True，否则返回False
    """
    # 质数定义：大于1的自然数，且只能被1和自身整除
    # 处理小于等于1的情况
    if num <= 1:
        return False
    # 2是唯一的偶质数
    if num == 2:
        return True
    # 偶数（除了2）都不是质数
    if num % 2 == 0:
        return False
    # 只需检查到平方根即可（优化性能），且只检查奇数
    # 因为如果num有大于其平方根的因数，必然有一个对应的小于平方根的因数
    max_divisor = int(num **0.5) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True

# 主程序逻辑
if __name__ == "__main__":
    while True:
        # 获取用户输入并处理异常
        try:
            user_input = input("请输入一个整数（输入'q'退出）：")
            
            # 退出条件
            if user_input.lower() == 'q':
                print("程序已退出")
                break
            
            # 转换为整数
            number = int(user_input)
            
            # 调用判断函数
            if is_prime(number):
                print(f"{number} 是质数")
            else:
                print(f"{number} 不是质数")
        
        # 处理非整数输入的异常
        except ValueError:
            print("输入错误！请输入有效的整数或'q'退出。")