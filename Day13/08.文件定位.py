

with open("demo08","r+",encoding="utf-8") as f:
    # print(f.read())
    f.seek(600)
    print(f.tell())