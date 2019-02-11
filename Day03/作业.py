# sum = 0
# for i in range(0,11):
#     if i % 2 == 0:
#         sum += i
# print(sum)

#
# for i in range(2,101):
#     f = 0
#     for j in range(2,i-1):
#         if i % j == 0:
#             f = 1
#             break
#     if f == 0:
#         print(i)


# count = 0
# for i in range(100, 1001):
#     if i % 5 == 0 and i % 6 == 0:
#         count += 1
#         print(i, "\t", end="")
#         if count % 5 == 0:
#             print()


# for i in range(97,122):
#     print(chr(i))
# for i in range(90,64,-1):
#     print(chr(i))

# sub = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sub -= 1.0/i
#     else:
#         sub += 1.0/i
#
# print("结果为:%.4f" % sub)

# count = 0
# for i in range(20,81):
#     if i % 3 == 0:
#         count += 1
#         print(i, "\t", end="")
#         if count % 5 == 0:
#             print()


# count = 0
# for i in range(1000,2001):
#     if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
#         count += 1
#         print(i, "\t", end="")
#         if count % 4 == 0:
#             print()



# for i in range(0,10):
#     for j in range(0,10):
#         if i +j == 12:
#             print(i,j)


# import random
#
# num = random.randint(0,9999)
# print(num)
# wei = len(str(num))
# print("该数共有%d位" % wei)
# ge = num % 10
# shi = num // 10 % 10
# bai = num // 100 % 10
# qian = num // 1000 % 10
# if wei == 1:
#     print("个位是%d" % wei)
# elif wei == 2:
#     print('十位是%d,个位是%d'%(shi,ge))
# elif wei == 3:
#     print('百位是%d,十位是%d,个位是%d'%(bai,shi,ge))
# elif wei == 4:
#     print('千位是%d,百位是%d,十位是%d,个位是%d'%(qian,bai,shi,ge))

# for a in range(0,10):
#     for b.txt in range(0,10):
#         for c in range(0,10):
#             for d in range(0,10):
#                 if (a * 10  + b.txt) + (c *10 +d) == (d *10 +a):
#                     print(a,b.txt,c,d)




# sum = 0
# for i in range(3, 100, 2):
#     sum += (i-2)/i
# print(sum)

# water = 15
# l = 0
# while water <= 50:
#     water += 5
#     l += 1
# print(l)



# day = 9
# t = 1
# while day > 0:
#     z = (t+1)*2
#     t = z
#     day -= 1
#
# print(z)


# height = 100.0
# H = height / 2
#
# for n in range(2, 11):
#     height += 2 * H
#     H /= 2
#
# print(height,H)

# import calendar
# print(calendar.calendar(2018))

# print(sum(range(1,102,4)) - sum(range(3,102,4)))

# sub = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sub -= 1.0/i
#     else:
#         sub += 1.0/i
# print("结果为:%.4f" % sub)

# import random
# num = random.randint(0,99999)
# print(num)
# wei = len(str(num))
# print("该数共有%d位" % wei)
# ge = num % 10
# shi = num // 10 % 10
# bai = num // 100 % 10
# qian = num // 1000 % 10
# wang = num // 10000
# if wei == 1:
#     print("个位是%d" % wei)
# elif wei == 2:
#     print('十位是%d,个位是%d'%(shi,ge))
# elif wei == 3:
#     print('百位是%d,十位是%d,个位是%d'%(bai,shi,ge))
# elif wei == 4:
#     print('千位是%d,百位是%d,十位是%d,个位是%d'%(qian,bai,shi,ge))
# elif wei == 5:
#     print('万位是%d,千位是%d,百位是%d,十位是%d,个位是%d'%(wang,qian,bai,shi,ge))

day = 9
t = 1
while day > 0:
    z = (t+1)*2
    t = z
    day -= 1

print(z)
























# print(sum(range(1,102,2)) - sum(range(3,102,4)))





