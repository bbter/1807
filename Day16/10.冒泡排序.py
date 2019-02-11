list01 = [1, 2, 4, 6, 4, 34, 57654, 5, 7, 8, 9, 4, 3, 235]



for i in range(0,len(list01)-1):
    print(list01[i])
    for j in range(0,len(list01)-1):
        if list01[j] > list01[j+1]:
            list01[j],list01[j+1] = list01[j+1],list01[j]

print(list01)

