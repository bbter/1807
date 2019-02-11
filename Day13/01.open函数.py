'''
open函数
    file,               目标文件,可以是相对路径,也可以是绝对路径
    mode='r',           打开的模式,读取/写入
    encoding=None,      写入的编码方式
    newline=None,       是字符串格式内容有: \n \r\n \t


'''

# f = open(file="demo.txt",mode="w+",encoding="utf-8")
# f.write("床前明月光,疑是地上霜,举头望明月,低头思故乡。\n")
# f.write("床前明月光,疑是地上霜,举头望明月,低头思故乡。")
# print(f.read())
# f.close()


with open("demo.txt","w+",encoding="utf-8") as f:
    f.write("床前明月光,疑是地上霜,举头望明月,低头思故乡。\n")
    f.write("床前明月光,疑是地上霜,举头望明月,低头思故乡。")
    f.flush()
    print(f.read())