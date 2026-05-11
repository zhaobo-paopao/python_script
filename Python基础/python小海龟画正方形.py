#用python语言实现画一个边长为99像素的正方形（用到变量）
import turtle    #‌Python中的Turtle是一个图形绘制库, Python 中一个内置模块,它提供了一个直观的接口来创建和控制屏幕上的图形,首先引入turtle库
#创建一个画布窗口
window=turtle.Screen()
#创建一个海龟对象
pen=turtle.Turtle()
#定义正方形边长
side_length=150
#绘制正方形
for _ in range(4):   #四个边界
    pen.forward(side_length)
    pen.right(90)
#关闭画布窗口
window.exitonclick()