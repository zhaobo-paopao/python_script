import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图表
plt.figure(figsize=(10, 6))  # 设置图形大小
plt.plot(x, y, label="sin(x)", color="red", linewidth=2)
plt.title("正弦函数", fontsize=16, fontweight="bold")
plt.xlabel("X轴", fontsize=12)
plt.ylabel("sin(X)", fontsize=12)
plt.legend()  # 显示图例
plt.grid(True, alpha=0.3)  # 添加网格
plt.show()


# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号

# 创建带有中文的图表
plt.figure(figsize=(8, 6))
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], "o-", label="数据线")
plt.title("中文标题示例")
plt.xlabel("横坐标")
plt.ylabel("纵坐标")
plt.legend()
plt.show()

# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 子图1：折线图
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), "b-", label="sin")
axes[0, 0].plot(x, np.cos(x), "r--", label="cos")
axes[0, 0].set_title("三角函数")
axes[0, 0].legend()

# 子图2：散点图
np.random.seed(42)
x = np.random.randn(100)
y = x + np.random.randn(100) * 0.5
axes[0, 1].scatter(x, y, alpha=0.6, c="green", edgecolors="black")
axes[0, 1].set_title("散点图")

# 子图3：柱状图
categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]
axes[1, 0].bar(categories, values, color=["red", "blue", "green", "orange"])
axes[1, 0].set_title("柱状图")

# 子图4：饼图
sizes = [15, 30, 45, 10]
labels = ["第一部分", "第二部分", "第三部分", "第四部分"]
axes[1, 1].pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
axes[1, 1].set_title("饼图")

plt.tight_layout()  # 自动调整子图间距
plt.show()


# 高级功能示例

# 3D图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)
ax.scatter(x, y, z, c=z, cmap="viridis")
ax.set_xlabel("X轴")
ax.set_ylabel("Y轴")
ax.set_zlabel("Z轴")
plt.show()
