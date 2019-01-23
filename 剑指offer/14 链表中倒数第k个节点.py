'''
题目：输入一个链表，输出该链表中倒数第k个结点。
'''

'''
使用列表的切片，还是很快的
28ms
5732k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []  #存放节点，不是存放节点的数值
        while head is not None:
            res.append(head)
            head = head.next
        #len(res)为链表长度，下面判断一下输入的k是否在1-len(res)之间
        if k > len(res) or k < 1:
            return
        return res[-k]