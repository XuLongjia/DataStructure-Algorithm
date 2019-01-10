#!usr/bin/python
#-*- coding:utf-8 -*-

def shellSort(ls):
    '''希尔排序，时间复杂度为n方，不稳定'''
    n = len(ls)
    gap = n//2
    while gap>=1:
        #下面其实就是插入算法，只不过换成了gap步长
        for j in range(gap,n):
            i = j
            while i >0:
                if ls[i] < ls[i-gap]:
                    ls[i],ls[i-gap] = ls[i-gap],ls[i]
                else:
                    break
                i -= gap
        #缩短步长
        gap //= 2
    return ls