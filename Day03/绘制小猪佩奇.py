import turtle as t
import time
'''
是一个简单的绘图工具

提供一个小海龟，可以把它理解为一个机器人，只能听得懂有限的命令

绘图窗口的原点(0,0)在正中间，默认海龟的方向是右侧

运动命令
forward(d) 向前移动d长度
backward(d) 向后移动d长度
right(d)   向右转动d度
left(d)   向左转动d度
goto(x,y)  移动到坐标为(x,y)的位置
speed(speed) 笔画绘制的速度[0,10]

笔画控制命令
up() 笔画抬起，在移动的时候不会绘图
down() 笔画落下，移动会绘图
setheading(d) 改变海龟的朝向
pensize(d)  笔画的宽度
pencolor(color) 笔画的颜色
reset() 恢复所有设置，清空窗口，重置turtle状态
clear() 清空窗口，不会重置turtle
circle(r,steps=e) 绘制一个圆形，r为半径，e为次数
begin_fill()
fillcolor(colorstr)
end_fill()

其他命令
done() 程序继续执行
undo() 撤销上一次动作
hideturtle() 隐藏海龟
showturtle() 显示海龟
screensize(x,y)
'''
t.screensize(1000,1000)

# t.speed(1)

# t.forward(100)
# t.right(45)
# t.forward(100)
# t.goto(-100,-200)
# t.up()
# t.goto(-100,100)
# t.down()
# t.pencolor('red')
# t.pensize(10)
# t.forward(80)
# t.setheading(50)

# t.reset()
# t.clear()

# t.circle(100)
# t.goto(100,50)
# t.begin_fill()
# t.fillcolor("blue")
# t.circle(50,steps=5)
# t.end_fill()
# t.forward(100)
# t.undo()
# t.hideturtle()






t.done()



# ***************************************小猪佩奇
'''
t.pensize(4) # 设置画笔的大小
t.colormode(255) # 设置GBK颜色范围为0-255
t.color((255,155,192),"pink") # 设置画笔颜色和填充颜色(pink)
t.setup(840,500) # 设置主窗口的大小为840*500
t.speed(10) # 设置画笔速度为10
#鼻子
t.pu() # 提笔
t.goto(-100,100) # 画笔前往坐标(-100,100)
t.pd() # 下笔
t.seth(-30) # 笔的角度为-30°
t.begin_fill() # 外形填充的开始标志
a=0.4
for i in range(120):
   if 0<=i<30 or 60<=i<90:
       a=a+0.08
       t.lt(3) #向左转3度
       t.fd(a) #向前走a的步长
   else:
       a=a-0.08
       t.lt(3)
       t.fd(a)
t.end_fill() # 依据轮廓填充
t.pu() # 提笔
t.seth(90) # 笔的角度为90度
t.fd(25) # 向前移动25
t.seth(0) # 转换画笔的角度为0
t.fd(10)
t.pd()
t.pencolor(255,155,192) # 设置画笔颜色
t.seth(10)
t.begin_fill()
t.circle(5) # 画一个半径为5的圆
t.color(160,82,45) # 设置画笔和填充颜色
t.end_fill()
t.pu()
t.seth(0)
t.fd(20)
t.pd()
t.pencolor(255,155,192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()
#头
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300,-30) # 顺时针画一个半径为300,圆心角为30°的园
t.circle(100,-60)
t.circle(80,-100)
t.circle(150,-20)
t.circle(60,-95)
t.seth(161)
t.circle(-300,15)
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)
a=0.4
for i in range(60):
   if 0<=i<30 or 60<=i<90:
       a=a+0.08
       t.lt(3) #向左转3度
       t.fd(a) #向前走a的步长
   else:
       a=a-0.08
       t.lt(3)
       t.fd(a)
t.end_fill()
#耳朵
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(-7)
t.seth(0)
t.fd(70)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,54)
t.end_fill()
t.pu()
t.seth(90)
t.fd(-12)
t.seth(0)
t.fd(30)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,56)
t.end_fill()
#眼睛
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-95)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-25)
t.seth(0)
t.fd(40)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()
#腮
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-95)
t.seth(0)
t.fd(65)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()
#嘴
t.color(239,69,19)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(-100)
t.pd()
t.seth(-80)
t.circle(30,40)
t.circle(40,80)
#身体
t.color("red",(255,99,71))
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-78)
t.pd()
t.begin_fill()
t.seth(-130)
t.circle(100,10)
t.circle(300,30)
t.seth(0)
t.fd(230)
t.seth(90)
t.circle(300,30)
t.circle(100,3)
t.color((255,155,192),(255,100,100))
t.seth(-135)
t.circle(-80,63)
t.circle(-150,24)
t.end_fill()
#手
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-40)
t.seth(0)
t.fd(-27)
t.pd()
t.seth(-160)
t.circle(300,15)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-10)
t.circle(-20,90)
t.pu()
t.seth(90)
t.fd(30)
t.seth(0)
t.fd(237)
t.pd()
t.seth(-20)
t.circle(-300,15)
t.pu()
t.seth(90)
t.fd(20)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-170)
t.circle(20,90)
#脚
t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(-75)
t.seth(0)
t.fd(-180)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)
t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(40)
t.seth(0)
t.fd(90)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)
#尾巴
t.pensize(4)
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(70)
t.seth(0)
t.fd(95)
t.pd()
t.seth(0)
t.circle(70,20)
t.circle(10,330)
t.circle(70,30)

time.sleep(10)
'''