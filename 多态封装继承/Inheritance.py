# 父类（基类）
# 核心思想：子类继承父类的属性和方法，可以扩展或修改
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f"{self.name} 正在吃东西")
    
    def sleep(self):
        print(f"{self.name} 正在睡觉")
    
    def make_sound(self):
        print("动物发出声音")

# 子类（派生类）
class Dog(Animal):  # Dog继承Animal
    def __init__(self, name, age, breed):
        # 调用父类的初始化方法
        super().__init__(name, age)
        # 添加子类特有的属性
        self.breed = breed
    
    # 重写父类方法（多态的基础）
    def make_sound(self):
        print(f"{self.name} 汪汪叫！")
    
    # 添加子类特有的方法
    def fetch(self):
        print(f"{self.name} 正在捡球")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} 喵喵叫～")
    
    def climb_tree(self):
        print(f"{self.color}的猫在爬树")

# 使用
my_dog = Dog("旺财", 2, "金毛")
my_cat = Cat("小花", 1, "白色")

print(f"狗的名字：{my_dog.name}")  # 继承自Animal
print(f"狗的品种：{my_dog.breed}")  # Dog特有的属性
my_dog.eat()      # 旺财 正在吃东西（继承的方法）
my_dog.make_sound()  # 旺财 汪汪叫！（重写的方法）
my_dog.fetch()    # 旺财 正在捡球（特有的方法）

my_cat.make_sound()  # 小花 喵喵叫～

# 继承的好处：
# 代码复用（不用重复写相同的代码）
# 建立类的层次关系
# 扩展功能很方便