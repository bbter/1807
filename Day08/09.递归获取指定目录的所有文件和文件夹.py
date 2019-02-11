import os
'''
os模块
    是对文件和文件夹执行操作的一个模块


'''
# 获取当前文件的路径
print(os.getcwd())
print(os.path.exists(os.getcwd()))

print(os.path.isdir(r"F:\QF1807\Day08"))

print(os.path.isfile(r"F:\QF1807\Day08\01.偏函数.py"))

listdir = os.listdir(r"F:\QF1807\Day08")
print(listdir)

def getAllDirRE(path,sp = ""):
    # 得到当前目录下所有的文件
    filesList = os.listdir(path)
    # 处理每一个文件
    sp += "  "
    for fileName in filesList:
        # 判断是否是路径(要用绝对路径)
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp+ "目录:",fileName)
            # 递归调用
            getAllDirRE(fileAbsPath,sp)
        else:
            print(sp + "普通文件",fileName)

# getAllDirRE(r"E:\培训记录")