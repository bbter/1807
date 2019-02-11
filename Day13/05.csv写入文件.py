'''
创建csv对象
csv.writer(fileobj)

放入一个可迭代对象,写在一行,每个元素为一列
csv_writer.writerow("hello")


放入一个可迭代类型的元素,这个元素中的每一个子元素也必须可迭代,
每个子元素占一行,子元素又会被拆开占据多列,长度取决于自身
csv_writer.writerows(Iterable(Iterable))
'''




import csv

with open("demo05.csv","w",encoding="utf-8") as f:
    # 创建csv
    csv_writer = csv.writer(f)
    # 写入内容
    csv_writer.writerow("hello")





















