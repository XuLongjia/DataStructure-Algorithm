'''
题目：输入一个链表，反转链表后，输出链表的所有元素。
'''

'''
pHead始终指向要反转的结点
last 指向反转后的首结点
每反转一个结点，把pHead结点的下一个结点指向last, last指向pHead成为反转后首结点, 再把pHead向前移动一个结点直至None结束

26ms
5852k
'''

#-*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None
        #每次循环last向后移动一个单位，链表也就增长一个单位

        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp
        return last




