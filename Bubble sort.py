'''
 Bubble sort
 Date: 2020-9-20

'''

lis = [int(i) for i in input().strip().split()]

n = len(lis)
for i in range(n):
    for j in range(n-1):
        if lis[j]>lis[j+1]:
            trans = lis[j+1]
            lis[j+1] = lis[j]
            lis[j] = trans
        print(lis)



