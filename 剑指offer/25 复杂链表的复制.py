'''
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

'''
思路：1. 根据旧链表创建新链表，不去管随机的那个指针
     2. 根据旧链表中的随机指针，创建新链表中的随机指针
     3. 从旧链表中拆分得到新链表

32ms
5632k
'''

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNodes(pHead)  #根据旧链表创建新链表，不去管随机的那个指针
        self.ConnectRandomNodes(pHead)  #根据旧链表中的随机指针，创建新链表中的随机指针
        return self.ReconnectNodes(pHead)   #从旧链表中拆分得到新链表
    # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面

    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            # pCloned.random = None         #不需要写这句话, 因为创建新的结点的时候,random自动指向None

            pNode.next = pCloned
            pNode = pCloned.next

    # 将复制后的链表中的复制结点的random指针链接到被复制结点random指针的后一个结点
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next   #pClonedHead是头，用来返回，pCloneNode是指针，一步步往后
        pNode.next = pClonedHead.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead


'''
华科平凡：

'''


#递归法
class Solution:
    def Clone(self, head):
        if not head: return
        newNode = RandomListNode(head.label)
        newNode.random = head.random
        newNode.next = self.Clone(head.next)
        return newNode

#哈希表法
class Solution:
    def Clone(self, head):
        nodeList = []  # 存放各个节点
        randomList = []  # 存放各个节点指向的random节点。没有则为None
        labelList = []  # 存放各个节点的值

        while head:
            randomList.append(head.random)
            nodeList.append(head)
            labelList.append(head.label)
            head = head.next
        # 每个random节点的索引（对应于nodeList的位置），如果为空则为-1
        labelIndexList = map(lambda c: nodeList.index(c) if c else -1, randomList)

        dummy = RandomListNode(0)
        pre = dummy
        # 节点列表，只要把这些节点的random设置好，顺序串起来就ok了。
        nodeList = map(lambda c: RandomListNode(c), labelList)  #此时nodeList变成了一个可迭代对象（从值到node)
        # 把每个节点的random绑定好，根据对应的index来绑定
        for i in range(len(nodeList)):
            if labelIndexList[i] != -1:
                nodeList[i].random = nodeList[labelIndexList[i]]
        for i in nodeList:
            pre.next = i
            pre = pre.next
        return dummy.next