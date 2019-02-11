import os
import re
filepath = r"F:\QF1807\Day20\test\东坡肉_百度百科_files" # 文件夹路径
delect = ".下载" # 要删东坡肉_百度百科_files除的名字字符串

for fileName in os.listdir(filepath):
    if delect in fileName:
        abspath = os.path.join(filepath,fileName)
        abspath2 = os.path.join(filepath,fileName[:-3])
        os.rename(abspath,abspath2)