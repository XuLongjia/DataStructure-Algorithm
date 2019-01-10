#!usr/bin/python
#-*- coding:utf-8 -*-

def mergerSort(ls):
    '''归并排序,时间复杂度为nlog(n),属于稳定排序，但是空间复杂度要比较高'''

    #递归的终止条件
    if len(ls) <= 1:
        return ls

    #否则：
    mid = len(ls)//2
    left = mergerSort(ls[:mid])
    right = mergerSort(ls[mid:])

    res = []
    l,r = 0,0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l +=1
        else:
            res.append(right[r])
            r +=1
    #循环结束后下面两行肯定一个为空列表，另外一个不是，顺序没关系
    res += left[l:]
    res += right[r:]

    return res

if __name__ =='__main__':
    ls = [0,9,8,7,6,5,4,3,2,1,-1,-2,-3]
    print(mergerSort(ls))