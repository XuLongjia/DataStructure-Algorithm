#!usr/bin/python
# -*- coding:utf-8 -*-

def insertSort(ls):
    '''插入排序，时间复杂度为n方，属于稳定排序'''
    n = len(ls)
    for j in range(1,n):
        i = j  #i代表内层
        #从右边取出一个元素，然后插入到左边正确的位置中
        while i >0:
            if ls[i] < ls[i-1]:
                ls[i],ls[i-1] = ls[i-1],ls[i]
            else:
                break   #如果上面的if语句没有执行说明序列已经有序啦，就不需要再往右边走了，相当于做了一个优化
            i -= 1
    return ls


if __name__ =='__main__':
    ls = [9,8,7,6,5,4,3,2,1,0]
    print(insertSort(ls))