'''
列表嵌套
L  = [[列表1],[列表2],[列表3]]
'''

name_list = ["张默", "宁财神", "李代沫", "房祖名", "柯震东", "高虎","张耀扬","满文军"]
sort_room =  [["张默", "宁财神",],["李代沫", "房祖名",],["柯震东", "高虎"]]
print(sort_room)

for room in sort_room:
    for name in room:
        print(name)

'''
有三个房间
有九个人
把这就九个人随机分配到三个房间
每个房间人数保持一致
'''
name_list = ["张默", "宁财神", "李代沫", "房祖名", "柯震东", "高虎","张耀扬","满文军"]
# 其实不存在多维列表,多维列表中的每一次元素
sort_room = [[],[],[]]


import random
for name in name_list:
        sort_room[random.randint(0,2)].append(name)
print(sort_room)





























