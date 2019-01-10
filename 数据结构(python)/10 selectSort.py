#!usr/bin/python
#-*- coding:utf-8 -*-

def selectSort(ls):
    '''选择排序,时间复杂度为n方，属于不稳定排序'''
    n = len(ls)
    for j in range(n-1):  #j  = 0,1,2,3...n-2  倒数第二个元素
        minIndex = j
        for i in range(j+1,n):  #每次遍历的次数
            if ls[minIndex] > ls[i]:
                minIndex = i
        ls[j],ls[minIndex] = ls[minIndex],ls[j]  #每次遍历结束后，将开头元素与最小元素交换位置
        #左边是排好序的，越来越多，右边越来越小
    return ls


if __name__ == "__main__":
    ls = [9,8,7,6,5,4,3,2,1]
    print(selectSort(ls))
