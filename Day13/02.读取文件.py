'''
read            一次读取文件所有内容
readline        每次读取一行内容
readlines       一次读取全部内容返回一个列表,每一行当作一个元素
'''



with open("demo02.txt","r",encoding="utf-8") as f:
    # content = f.read()
    content = f.readlines()
    print(content)

    # f.write("白日依山尽,黄河入海流。\n")
    # f.write("欲穷千里目,更上一层楼.")