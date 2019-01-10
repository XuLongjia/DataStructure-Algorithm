#!usr/bin/python
#-*- coding:utf-8 -*-

def quickSort(ls,first,last):
    '''快速排序，时间复杂度为n方，不稳定排序，应用最多，必须掌握！'''
    #递归终止条件
    if first >= last:
        return

    mid_value = ls[first]
    low = first
    high = last

    while low < high:
        while low<high and ls[high] > mid_value:
            high -=1
        ls[low] = ls[high]
        while low<high and ls[low] < mid_value:
            low +=1
        ls[high] = ls[low]
    ls[low] = mid_value

    quickSort(ls,first,low) #左边进行排序
    quickSort(ls,low+1,last)  #右边进行排序

if __name__ =="__main__":
    ls = [9,8,7,6,5,4,3,2,1,0,-1,-2]
    quickSort(ls,0,len(ls)-1)
    print(ls)