'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

'''
第三位是前两位之和，一直迭代的
30ms
5848k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1]   #注意，第一个0只是为了补位，可以没有
        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return res[n]
        #30ms 5848K

    def fibonaccis(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        res = [1,1]
        while len(res)<n:
            res.append(res[-1]+res[-2])
        return res[-1]
        # 30ms.5872k