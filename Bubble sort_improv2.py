'''
 Bubble sort
 Date: 2020-9-20
 improv2：优化内层循环
    记住最后一次交换发生位置lastExchange, 之后的为有序的，可减少排序趟数。
'''

lis = [int(i) for i in input().strip().split()]
n = len(lis)
LastExchange = n-1

for i in range(n):
    flag = 0
    for j in range(n-1):
        print("i为",i,"; j为",j)
        if j > LastExchange:   # improve2,记录最后一次交换顺序的位置
            break

        if lis[j]>lis[j+1]:
            trans = lis[j+1]
            lis[j+1] = lis[j]
            lis[j] = trans
            flag = 1
            LastExchange = j
        # print(lis)

# improv1: 当数字没有交换时，则代表顺序已排列好，则可直接跳出循环
    if flag == 0:
        print(lis)
        exit()



