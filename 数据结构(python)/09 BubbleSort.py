#!usr/bin/python
# -*- coding:utf-8 -*-

def bubbleSort(ls):
    '''冒泡排序，时间复杂为n方，属于稳定排序'''
    for j in range(len(ls)-1,0,-1):
        #每次减少迭代次数
        for i in range(j):
            if ls[i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
    return ls

#改进版：
def bubbleSort_2(ls):
    '''冒泡排序，时间复杂为n方，属于稳定排序'''
    for j in range(len(ls)-1,0,-1):
        #每次减少迭代次数
        count = 0   #加一个计数器，如果某次循环没有进行元素交换，则说明前面全部都是有序的，则直接终止
        for i in range(j):
            if ls[i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                count += 1
        if count == 0:
            return
    return ls

if __name__ == "__main__":
    ls = [9,8,7,6,5,4,3,2,1,0]
    print(bubbleSort(ls))
