class Pet:
    """宠物基类"""
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.__health = 100  # 私有属性（完全封装）
    
    # 封装：通过方法访问私有属性
    def get_health(self):
        return self.__health
    
    def see_doctor(self):
        self.__health = min(100, self.__health + 30)
        print(f"{self.name} 看了医生，健康值恢复")
    
    # 多态：定义通用接口
    def speak(self):
        raise NotImplementedError("子类必须实现speak方法")

class Dog(Pet):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed
        self.__bones = 0  # 私有属性
    
    # 多态：实现自己的speak
    def speak(self):
        return f"{self.name}: 汪汪！我是{self.breed}"
    
    # 子类特有方法
    def dig_hole(self):
        print(f"{self.name} 正在挖洞")

class Cat(Pet):
    def __init__(self, name, owner, color):
        super().__init__(name, owner)
        self.color = color
    
    def speak(self):
        return f"{self.name}: 喵～我是{self.color}的猫"
    
    def catch_mouse(self):
        print(f"{self.name} 在抓老鼠")

class Parrot(Pet):
    def __init__(self, name, owner, can_talk):
        super().__init__(name, owner)
        self.can_talk = can_talk
    
    def speak(self):
        if self.can_talk:
            return f"{self.name}: 你好！我是鹦鹉"
        else:
            return f"{self.name}: 啾啾！"

# 使用多态
pets = [
    Dog("旺财", "小明", "金毛"),
    Cat("咪咪", "小红", "白色"),
    Parrot("小绿", "小李", True)
]

# 多态的威力：统一处理不同类型的对象
for pet in pets:
    print(pet.speak())  # 每个宠物用自己的方式说话
    pet.see_doctor()    # 都能看医生
    
    # 检查是否有特定方法
    if hasattr(pet, 'dig_hole'):
        pet.dig_hole()
    elif hasattr(pet, 'catch_mouse'):
        pet.catch_mouse()

# 输出：
# 旺财: 汪汪！我是金毛
# 旺财 看了医生，健康值恢复
# 旺财 正在挖洞
# 咪咪: 喵～我是白色的猫
# 咪咪 看了医生，健康值恢复
# 咪咪 在抓老鼠
# 小绿: 你好！我是鹦鹉
# 小绿 看了医生，健康值恢复