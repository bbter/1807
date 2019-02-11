
dict1 = {}
with open("a.lrc","r",encoding="utf-8") as f:
    content = f.readlines()
    # print(content)
    for word in content:
        # print(word)
        new_wordList = word.replace("[","]").strip().split("]")
        for i in range(len(new_wordList)-1):
            if new_wordList[i]:
                dict1[new_wordList[i]] = new_wordList[-1]


# print(dict1)

for key in sorted(dict1.keys()):
    print(key, dict1[key])
