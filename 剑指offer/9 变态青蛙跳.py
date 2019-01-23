'''
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
'''

'''
因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
跳1级，剩下n-1级，则剩下跳法是f(n-1)
f(0) = 1 表示一次跳完
n = 1: 1
n =2 : 2
n =3 :f(3) = f(0)+ f(1) +f(2) =4
n =4:f(4) = f(0) + f(1) +f(2) + f(3)=2f(3) = 8
所以f(n) = 2**(n-1)
37ms
5752k
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)