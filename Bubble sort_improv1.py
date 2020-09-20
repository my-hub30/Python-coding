'''
 Bubble sort
 Date: 2020-9-20
 improv1：优化外层循环
    引入一个标签flag, 当数字没有交换时，则代表顺序已排列好，则可直接跳出循环
'''

lis = [int(i) for i in input().strip().split()]
n = len(lis)

for i in range(n):
    flag = 0
    for j in range(n-1):
        if lis[j]>lis[j+1]:
            trans = lis[j+1]
            lis[j+1] = lis[j]
            lis[j] = trans
            flag = 1
        print(lis)

# improv1: 当数字没有交换时，则代表顺序已排列好，则可直接跳出循环
    if flag == 0:
        print(lis)
        exit()



