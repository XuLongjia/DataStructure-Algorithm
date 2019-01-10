#!usr/bin/python
#-*- coding:utf-8 -*-

'''二分查找，也叫折半查找，时间复杂度为log(n)'''

def bin_search(ls,item):
    '''递归版本'''
    n = len(ls)
    if n >0:
        mid = n//2
        if ls[mid] == item:
            return True
        elif ls[mid] >item:
            return bin_search(ls[:mid],item)
        else:
            return bin_search(ls[mid+1:],item)
    return False

def bin_search2(ls,item):
    '''非递归版本'''
    low = 0
    high = len(ls)-1
    while low <= high:
        mid = int((low+high)/2)
        if ls[mid] == item:
            return mid
        elif ls[mid] > item:
            high = mid-1
        else:
            low = mid+1
    return None

if __name__ =='__main__':
    ls = [1,2,3,4,5,6,7,8,9,10]
    print('递归版本：')
    print(bin_search(ls,5))
    print(bin_search(ls,100))
    print('非递归版本：')
    print(bin_search2(ls,5))
    print(bin_search2(ls,999))