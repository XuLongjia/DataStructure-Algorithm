'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
方法一： 两个数组相加
38ms
5752k
'''

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        l = [i for i in array if i%2 == 1]
        r = [i for i in array if i%2 == 0]
        return l+r

'''
方法二：类似冒泡的思想，相互交换
'''
