#用python语言实现画一个边长为93的正十边形，提示，往右旋转36
import turtle
#创建一个画布
canvas=turtle.Screen()
#创建一个海龟对象
pen=turtle.Turtle()
#设置画笔的初始位置和朝向
pen.penup()               #抬笔
pen.goto(-100,0)          #移动到指定 坐标，不改变方向
pen.pendown()             #落笔
#设置画笔的颜色和线条粗细
pen.color("blue")  #画笔颜色
pen.pensize(2)     #画笔粗细
#绘制十边形
for _ in range(10):
    pen.forward(93)  #按照像素长度向前走,
    pen.right(36)    #按照角度向右转
#关闭画布
canvas.exitonclick()

