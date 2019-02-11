import tkinter
def func():
    print("bbt is a good man")
# 创建窗口对象
window = tkinter.Tk()
# 设置窗口标题
window.title("我的第一个窗口")
# 设置窗口尺寸,参数以字符串的形式编写,前面是宽和高，用小写的x连接,后面是屏幕中的位置用+号连接
window.geometry("800x800+1000+200")

button1 = tkinter.Button(window,text="按钮",command=func,width = 30,height = 10)

button1.pack()

button2 = tkinter.Button(window,text="退出",width = 30,height = 10,command=window.quit)
button2.pack()

# 框架
frame = tkinter.Frame(window,width = 100,bg="red")
frame.pack()




window.mainloop()