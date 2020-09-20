'''
 Dijkstra smallest pathway
    find the smallest pathway from A to other vertice
 Date: 2020-9-18

 NB: 直接运行错误，但在console中运行正确时，检查python代码的tab是否对齐
'''

# 生成小写字母：  vertice = [chr(i) for i in range(97,103)]

import numpy as np                  # 生成大写字母
aaa = np.arange(65,71)              # 生成大写字母
vertice = [chr(i) for i in aaa]     # 生成大写字母
ver_num = len(vertice)
MAX= float('inf')
matrix = [                  # 路径矩阵
    #A B  C   D E    F
    [0,10,MAX,4,MAX,MAX],   # A  matrix[0] 第一行
    [10,0,8,2,6,MAX],       # B
    [MAX,8,10,15,1,5],      # C
    [4,2,15,0,6,MAX],       # D
    [MAX,6,1,6,0,12],       # E
    [MAX,MAX,5,MAX,12,0]    # F
    ]
opt_dst = [MAX] * len(matrix)   # the optimal distance from A to others
opt_dst[0] = 0

SmaPathVer = ['A']  # smallest pathway vertice list
opt_ver = 'A'


while len(SmaPathVer) <=  len(matrix)-1:
    # 更新opt_dst
    for i in range(ver_num):
        if vertice[i] in SmaPathVer:
            opt_dst[i] = opt_dst[i]
        else:
            # print(i)
            para = ord(opt_ver)-65    # 大写字母 ——> int
            # print(para)
            opt_dst[i] = min(opt_dst[i], opt_dst[para]+matrix[para][i]) ###
            # print(opt_dst[i])

    # 更新下一个最佳路径的节点
    minnum = max(opt_dst)
    for i in range(ver_num):
        if vertice[i] in SmaPathVer:
            continue
        else:
            if opt_dst[i] <= minnum:
                minnum = opt_dst[i]
                opt_ver = chr(65+i)
    SmaPathVer.append(opt_ver)


print(opt_dst)


