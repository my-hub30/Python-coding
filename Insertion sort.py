'''
 Insertion sort
 Date: 2020-9-20

'''

a = [int(i) for i in input().strip().split()]
n = len(a)
for i in range(1,n):
    # print(a)
    for j in range(i,0,-1):
        if a[j] < a[j-1]:
            # print(j,'a[j-1]=',a[j-1], 'a[j]=',a[j])
            a[j-1], a[j] = a[j], a[j-1]
            # print(a[j-1],a[j])
        else:
            break

print(a)
