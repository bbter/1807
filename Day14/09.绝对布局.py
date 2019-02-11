'''
place
    x =
    y =


'''

import tkinter

window = tkinter.Tk()

window.geometry("400x400")

button01 = tkinter.Button(window,text="BTN01",bg="blue")

button01.place(x=30,y=30)



button02 = tkinter.Button(window,text="BTN02",bg="red")

button02.place(x=60,y=30)



window.mainloop()























