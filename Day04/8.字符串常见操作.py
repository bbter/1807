'''
字符串长见操作
        下标:index 从0开始，到len(str)-1
        切片:截取字符串中一部分内容
                str[start,stop,step]
                不包含stop位置的元素
'''
str00 = "床前明月光，疑是地上霜。举头望明月，低头思故乡。"

for w in str00:
    print(w,end="\t")


print(str00[9])

print(str00[0:5:2])

print(str00[:5])

print(str00[:])

print(str00[::])

print(str00[-1])

print(str00[:-1])

print(str00[::-1])

print(str00[-5:-10:-1])

print(str00[5:-10])



str01 = "唧唧复唧唧，木兰当户织，不闻机杼声，为闻女叹息"

# 切割字符串，以传入的文字切割,可以控制切割的份数
print(str01.split("唧",1))
print(str01.split("闻"))


str02 = "北国风光，千里冰封，万里飘飘，望长城内外，惟余莽莽，大河上下顿失滔滔"

# 查找指定字符在目标中的位置，可以指定范围，如果没有访问-1
print(str02.find("，",5))
print(str02.find("，",5,8))

# index()查看元素下标，，可以指定范围，如果没有会报错

print(str02.index("，"))
print(str02.index("，",5))
# print(str02.index("，",5,8))

# count()查看指定元素在字符串中的次数，可以指定范围，如果没有返回0
print(str01.count("唧"))
print(str01.count("无阿拉蕾"))


# replace() 替换目标中的元素，可以指定元素个数，如果替换失败返回原字符串
print(str01.replace("唧唧","jiji",1))
print(str01)


# capitalze()把第一个字符大写,其余全部小写


str03 = "life is short,you need Python"
print(str03.capitalize())

# title() 把每一个单词的首字母大写，其余小写
print(str03.title())

# swapcase() 大小写转换
print(str03.swapcase())

# startswith() 在给定的范围内判断是否是以给定的字符串开头，如果没有指定范围，默认整个字符串
print(str03.startswith("life"))

# endswith() 在给定的范围内判断是否是以给定的字符串开头，如果没有指定范围，默认整个字符串
print(str03.endswith("Python"))

'''
 lower()  把字母转换为小写
 upper()  把字母转换为大写
 islower() 判断是否全为小写
 isupper() 判断是否全为大写


'''
print(str03.lower())
print(str03.upper())
print(str03.islower())
print(str03.isupper())


# str.center(width,[,fillchar])
# 返回一个指定宽度的居中字符串，fillchar为填充的字符串，默认空格填充
str25 = "BBT is a Good Man!"
print(str25.center(40,'*'))

# ljust(width,[,fillchar])
# 返回一个指定宽度的左对齐字符串，fillchar为填充字符，默认空格填充
str26 = "BBT is a Good Man!"
print(str26.ljust(40,"%"),"*")


# rjust(width,[,fillchar])
# 返回一个指定宽度的右对齐字符串，fillchar为填充字符，默认空格填充
str27 = "BBT is a Good Man!"
print(str26.rjust(40,"%"))


# str.zfill(width)
# 返回一个长度为width的字符串，原字符串右对齐，前面补0
str28 = "BBT is a Good Man!"
print(str28.zfill(40))


'''
strip()去除两端的空字符
rfind() 从右侧查找
rindex() 从右侧查找索引
partition() 以传入内容分割三部分

'''
str5 = "    hello    "
print(str5.strip())
print(str01.rfind("唧"))

str6 = "helloWorld"
print(str6.partition("l"))


