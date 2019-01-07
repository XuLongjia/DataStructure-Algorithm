#!usr/bin/python
# -*- coding:utf-8 -*-

'''
来源于bilibili：up主：正月点灯笼
给定一个集和，arr = {3,34,4,12,5,2}，S = 9, 请问集合中是否可以找出一些数相加等于S
设subset(i,s) i表示结合的索引，s表示数字 比如原问题为 subset(arr[5],5,9)
选还是不选？  如果选了的话 subset(arr[5],5,9) = subset(arr[4],4,9-arr[5])
            不选  subset(arr[5],5,9) = subset(arr[4],4,9)
终止条件？
1、当s = 0 直接return True
2、当 arr[0]  直接return arr[0] == s
3、当 arr[i] > s,肯定是不选  直接 return subset(arr,i-1,s)

'''

import numpy as np

def rec_subset(arr,i,s):
    if s ==0:
        return True
    elif i==0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr,i-1,s)
    else:
        A = rec_subset(arr,i-1,s)
        B = rec_subset(arr,i-1,s-arr[i])
        return A or B

'''
非递归应该怎么写？ 考虑一个len(arr) *S+1 的矩阵：
        
arr   i   j= 0   1   3   4   5   6   7   8   9
3     0      F   F   T   F   F   F   F   F   F 
34    1   
4     2
12    3
5     4
2     5
'''
def dp_subset(arr,S):
    subset = np.zeros((len(arr),S+1),dtype = bool)
    subset[:,0] = True
    subset[0,:] = False
    subset[0,arr[0]] = True
    for i in range(1,len(arr)):
        for s in range(1,S+1):
            if arr[i] > s:
                subset[i,s] = subset[i-1,s]
            else:
                A = subset[i-1,s-arr[i]]
                B = subset[i-1,s]
                subset[i,s] = A or B
    r,c = subset.shape
    return subset[r-1,c-1]

def main():
    arr = [3,34,4,12,5,2]
    for i in range(9,14):
        print(rec_subset(arr,len(arr)-1,i))
    print('-----------------------')
    for i in range(9,14):
        print(dp_subset(arr,i))

if __name__ =='__main__':
    main()
