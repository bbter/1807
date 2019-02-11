with open("dict.txt","r") as f:
    dict_list = f.readlines()
    word = input("请输入你想要查询的单词:")
    for dict_item in dict_list:
        dict_en = dict_item.split("\t")
        if word.upper() == dict_en[0].upper():
            print(dict_en[0]+":"+dict_en[1])
            break
    else:
        print("尽情期待")
