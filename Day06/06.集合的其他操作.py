'''
集合的其他操作
        difference
            返回第一个集合中和第二个集合中不同的元素
            不改变原来集合
        difference_update
            返回第一个集合中和第二个集合中不同的元素
            改变原来集合
        intersection
            交集
        union
            并集
        symmetric_difference
            对称差


'''

set00 = set("床前明月光，疑是地上霜。")
set01 = set("明月几时有，把酒问青天。")

# 返回第一个集合中和第二个集合中不同的元素--->去除第一个集合和第二个集合重复的元素
print(set00.difference(set01))

print(set00)


# print(set00.difference_update(set01))
# print(set00)

# 取交集
print(set00.intersection(set01))

# 取并集
print(set00.union(set01))

# 取出两个集合中不同的元素组成一个新集合
print(set00.symmetric_difference(set01))



















