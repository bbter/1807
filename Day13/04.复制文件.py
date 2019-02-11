'''
读取本地指定文件所有内容
写入到一个新的文件

'''
import time
start_time = time.time()
with open("eason.mp3","rb+") as f:
    #读取文件内容
    content = f.read()

with open("eason_copy.mp3","wb+") as f:
    #写入文件内容
    f.write(content)

end_time = time.time()
print("消耗总时间为%s" %(end_time - start_time))



