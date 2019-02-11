'''
浮雕布局可以让控件以3D的效果呈现
浮雕布局属性为relief，共有五种类型：
FLAT —平的
RAISED —凸起的
RIDGE —脊状边缘
SUNKEN —凹陷
GROOVE —沟状
'''

import tkinter
window = tkinter.Tk()

window.geometry("400x400")

button01 = tkinter.Button(window,text="BTN01",bg="red",relief="flat")
button01.grid(row=1,column=1)

button01 = tkinter.Button(window,text="BTN01",bg="blue",relief="raised")
button01.grid(row=2,column=2)

window.mainloop()


























