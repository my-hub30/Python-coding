'''
 Selection sort
 Date: 2020-9-20

'''

lis = [int(i) for i in input().strip().split()]
n = len(lis)

for i in range(n-1):
    minnum = max(lis)   # initial
    for j in range(i,n):
        if lis[j] < minnum:  # 找到min后，互换位置
            minnum = lis[j]
            idx = j

    lis[i], lis[idx] = lis[idx],lis[i]   # exchange two items
    # print('i=',i,'idx=',idx,lis)








