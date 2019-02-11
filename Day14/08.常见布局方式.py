'''
相对布局
    pack
        side = left/right/top/bottom
'''
import tkinter

window = tkinter.Tk()

window.geometry("400x400")

button = tkinter.Button(window,text="BTN",bg="yellow")

button.pack()

window.mainloop()





















