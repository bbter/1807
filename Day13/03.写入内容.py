'''

write           参数是字符串,顺序写入内容,后一次紧跟前一次的末尾
writelines      参数是列表或者是字符串
'''



with open("demo03.txt","w",encoding="utf-8") as f:
    f.write("唧唧复唧唧,木兰当户织")
    f.write("不闻机杼声,惟闻女叹息")
    f.writelines(['白日依山尽,黄河入海流。\n', '欲穷千里目,更上一层楼.'])




