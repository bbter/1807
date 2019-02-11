'''
if语句嵌套的格式
if 条件1:
    满足条件1，做事情1
    满足条件1，做事情2
    满足条件1，做事情3
    .....(省略)
    if 条件2：
        满足条件2，做事情1
        满足条件2，做事情2
        满足条件2，做事情3

说明：外层的if判断，if...else
      内层   if...else
'''

ticket = input("你有票吗？(有=1，没有=0)：")
if ticket == "1":
    print("请经过安检")
    # 过安检
    knife_len = int(input("请说明你携带刀子的长度(厘米):"))
    if knife_len < 15:
        print("通过安检，可以上车")
    else:
        print("请跟我走一趟")
else:
    print("请先去买票")



































