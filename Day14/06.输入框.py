import tkinter

# 创建窗口对象
window = tkinter.Tk()
# 设置窗口标题
window.title("我的第一个窗口")
# 设置窗口尺寸,参数以字符串的形式编写,前面是宽和高，用小写的x连接,后面是屏幕中的位置用+号连接
window.geometry("400x400+1000+200")

# 框架容器
farme = tkinter.Frame(window,width=300,height=30)

farme.pack(side="top")

# 输入框
entry = tkinter.Entry(farme,width=30)
entry.pack(side="left")


def show():
    print(entry.get())

# 按钮
bin_in = tkinter.Button(farme,text="退出")
bin_in.pack(side="right")

bin_in = tkinter.Button(farme,text="查询",command=show)
bin_in.pack()


txt = tkinter.Text(window,width=40,height=30)
txt.pack()


window.mainloop()