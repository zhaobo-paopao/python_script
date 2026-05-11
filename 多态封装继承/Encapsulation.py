# 核心思想：把数据（属性）和操作（方法）包装在一起，隐藏内部细节
class Animal:
    def __init__(self, name, age):
        # 私有属性（封装）
        self._name = name
        self._age = age
        self._energy = 100  # 内部状态，外部不应该直接修改
    
    # 公有方法（接口）
    def eat(self, food):
        if self._energy < 100:
            self._energy += 20
            print(f"{self._name} 吃了 {food}，体力恢复了")
        else:
            print(f"{self._name} 还不饿")
    
    def get_energy(self):
        """获取当前体力（不暴露具体实现）"""
        if self._energy > 80:
            return "体力充沛"
        elif self._energy > 50:
            return "体力一般"
        else:
            return "需要进食"
    
    def get_info(self):
        return f"{self._name},{self._age}岁"

# 使用
cat = Animal("咪咪", 3)
print(cat.get_info())  # 咪咪，3岁
cat.eat("鱼")          # 咪咪 吃了 鱼，体力恢复了
print(cat.get_energy())  # 获取状态，而不是直接访问 _energy

# ❌ 不应该这样做（破坏了封装）
# cat._energy = 0  # 直接修改内部状态

# 封装的好处：
# 隐藏内部实现细节
# 保护数据完整性（比如体力值不能超过100）
# 修改内部实现不影响外部使用