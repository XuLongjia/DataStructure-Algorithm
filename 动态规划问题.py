#!usr/bin/python
# -*- coding:utf-8 -*-

'''
来源于bilibili：up主：正月点灯笼
给定一个数组，比如arr=[1,2,4,1,7,8,3]
要求，选择一堆数字，不能相邻，使得选中的数字相加的和最大
使用动态规划求解，选还是不选的问题，递推公式：opt(6) 的分支为 opt(5) 或者 opt(4) + arr[6]
opt(5) 分支为 opt(4) 或者opt(3) + arr[5]
opt(i) = arr[i] + opt(i-2)  或者 opt(i-1)
递归出口：opt(0) = arr[0]   opt(1) = max(arr[0],arr[1])
'''
import numpy as np

def rec_opt(arr,i):
    '''
    使用递归形式来求解
    '''
    if i == 0:
        return arr[0]
    elif i ==1:
        return max(arr[0],arr[1])
    else:
        A = rec_opt(arr,i-2) + arr[i]
        B = rec_opt(arr,i-1)
        return max(A,B)
def dp_opt(arr):
    '''
    使用非递归来求解
    opt[i]表示子问题的最优解
    '''
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt[len(arr)-1]

def main():
    arr = [1,2,4,1,7,8,3]
    print(rec_opt(arr,len(arr)-1))
    print(dp_opt(arr))

if __name__ == '__main__':
    main()
