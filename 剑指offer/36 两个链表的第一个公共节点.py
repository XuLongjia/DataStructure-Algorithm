'''
题目：输入两个链表，找出它们的第一个公共结点
'''

'''
思路：共同节点，意味着从共同节点开始之后所有的节点数都是相同的，这是链表，只要有一个共同节点，那么之后所有的指向
也是重复的。
先依次遍历两个链表，记录两个链表的长度m和n，
如果 m > n，那么我们就先让长度为m的链表走m-n个结点，然后
两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。

32ms
5632k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getLength(self,pHead):
        L = 0
        while pHead is not None:
            pHead = pHead.next
            L += 1
        return L
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        L1 = self.getLength(pHead1)
        L2 = self.getLength(pHead2)
        if L1>= L2:
            long = pHead1
            short = pHead2
        else:
            long = pHead2
            short = pHead1
        #让长链表先把差值走掉
        for i in range(abs(L1-L2)):
            long = long.next
        while long != short:
            long = long.next
            short = short.next
        return long