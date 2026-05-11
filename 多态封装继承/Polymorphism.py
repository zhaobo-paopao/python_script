# 核心思想：同一个接口，不同的实现
# 多态的经典例子
class Animal:
    def make_sound(self):
        pass  # 抽象方法，子类必须实现


class Dog(Animal):
    def make_sound(self):
        return "汪汪！"


class Cat(Animal):
    def make_sound(self):
        return "喵喵～"


class Bird(Animal):
    def make_sound(self):
        return "叽叽喳喳"


class Cow(Animal):
    def make_sound(self):
        return "哞～"


# 关键点：处理函数不关心具体是什么动物
def animal_concert(animals):
    """让一群动物开演唱会"""
    for animal in animals:
        # 重要：这里不知道具体是什么动物
        # 但知道它们都有 make_sound 方法
        print(animal.make_sound())


# 创建不同种类的动物
animals = [Dog("旺财"), Cat("咪咪"), Bird("小黄"), Cow("大牛")]

# 多态的体现
animal_concert(animals)
# 输出：
# 汪汪！
# 喵喵～
# 叽叽喳喳
# 哞～
