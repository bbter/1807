import tkinter


# 创建主窗口
window = tkinter.Tk()

window.title("Lable")

window.geometry("800x800+1000+200")

# win:父窗体
# text 显示的文本内容
# bg 背景色
# fg 字体颜色
# wraplength 指定text文本中多宽进行换行
# justify 设置换行后的对齐方式
# anchor 位置 n北 e东 s南 x西
label = tkinter.Label(window,
                      text="bbt is a good man",
                      bg = "pink",
                      fg = "red",
                      font = ("黑体",30),
                      width = 100,
                      height = 100,
                      wraplength = 400,
                      justify ="left",
                      anchor = "center")

label.pack()
window.mainloop()