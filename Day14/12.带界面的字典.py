

import tkinter
def search(word):
    with open("dict.txt") as file:
        dict_list = file.readlines()
        for dict00 in dict_list:
            dict_item = dict00.split("\t")
            if word.upper() == dict_item[0].upper():
                return "%s : %s" % (dict_item[0],dict_item[1])
        else:
            return "您查询的单词为收入,敬请期待。。。。\n"

def search_word():
    word = entry.get().strip()
    if len(word) != 0:
        # 执行搜索的方法,获取搜索的内容
        result = search(word)
        # 把结果插入到文本显示框
        txt.insert(tkinter.INSERT,result)
    else:
        txt.insert(tkinter.INSERT, "不能为空\n")

# 创建主窗口
window = tkinter.Tk()

# 添加标题
window.title("千锋字典")

# 设置窗口大小
window.geometry("400x400",)

# 主窗口内部的框架
frame = tkinter.Frame(window,width=300,height=30,bg="black")
frame.place(x=50,y=10)
# 输入框
entry = tkinter.Entry(frame,width=30)
entry.pack(side="left")

# 按钮
btn_in = tkinter.Button(frame,text="查询",width=5,command=search_word,bg="red")
btn_in.pack(side="right",pady=5)

# 按钮
btn_in = tkinter.Button(frame,text="退出",width=5,command=frame.quit,bg="red")
btn_in.pack(side="right",pady=5)

scroll_bar = tkinter.Scrollbar()

scroll_bar.pack(side="right",fill=tkinter.Y)

# 内容显示框
txt = tkinter.Text(window,width=50,height=25,bg="red")
txt.pack(side="bottom",pady=15)

txt.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=txt.yview)
# 显示
window.mainloop()