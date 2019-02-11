import os



file_lists = os.listdir()
file_lists.pop()
for name in file_lists:
    new_name = "[千锋出品] - " + name
    os.rename(name,new_name)
