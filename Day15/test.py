#
# with open("a.lrc","r",encoding="utf-8") as f:
#     content = f.readlines()
#     for word in content:
#         new_wordList = word.split("]")
#         for word2 in new_wordList:
#             new_wordList2 = word2.split("[")
#             for i in new_wordList2:
#                 if i != "" and i != "\n":
#                     print(i)




# 打开文件
# file = open("a.lrc", "r", encoding="utf-8")
#
# lrc_list = file.readlines()
# print(lrc_list)
#
# lrc_dict = {}
# # 遍历所有元素,干掉方括号
# for i in lrc_list:
#     # print(i)
#     # i.replace("[", "]")
#     print(i.replace("[", "]").split("]"))
#     # 取出方括号并切割歌词字符串
#     lrc_word = i.replace("[", "]").strip().split("]")
#     print(lrc_word)
#     for j in range(len(lrc_word) - 1):
#         if lrc_word[j]:
#             # print(lrc_word[j], end=",")
#             lrc_dict[lrc_word[j]] = lrc_word[-1]
# # 遍历字典,对字典的key进行排序,
# for key in sorted(lrc_dict.keys()):
#     print(key, lrc_dict[key])
#
# file.close()





import time




def XXX(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("总耗时：%s" % (end - start))
    return inner




@XXX
def hexin():
    time.sleep(3)
    print("核心代码")



hexin()


