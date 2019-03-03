'''
题目：一个链表中包含环，请找出该链表的环的入口结点。
'''

'''
思路：链表指针区只能指向一个下一个节点，所以如果链表中由环一定是在尾部。
寻找链表中环的入口结点主要分成三个步骤：
1\首先是设置两个快慢指针，如果快慢指针相遇，则快慢指针必然都在环中；
2\然后从相遇的地方设置一个指针向后遍历并记录走的步数，当这个指针重新指到开始的位置的时候，当前对应的步数就是
环中结点的数量k；
3\然后设置两个指针从链表开始，第一个节点先走k步，然后第二个指针指到链表的开始，两个指针每次
都向后走一步，两个指针相遇的位置就是链表的入口。

程序可以运行，但在牛客网上报错 'NoneType' object has no attribute 'next' 不知道为什么？？
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        MeetingNode = self.MeetingNode(pHead)
        if not MeetingNode:
            return None
        NodeOfLoop = 1
        FlagNode = MeetingNode
        # 从相遇点定义一个指针，指针向后移动到相遇点即为环的节点数NodeOfLoop
        while FlagNode.next != MeetingNode:
            NodeOfLoop += 1
            FlagNode = FlagNode.next

        # 两个指针都位于首位，让其中一个节点向前走环的节点数步，然后第二个指针走，当两个指针相遇时，即为环节点入口
        pFast = pHead
        pSlow = pHead
        for i in range(NodeOfLoop):
            pFast = pFast.next
        while pSlow != pFast:
            pSlow = pSlow.next
            pFast = pFast.next
        return pFast

    # 定义快慢指针，如果有环，快慢指针一定会相遇
    def MeetingNode(self, pHead):
        if not pHead:
            return None
        pSlow = pHead.next
        pFast = pSlow.next
        while pSlow != pFast:
            pSlow = pSlow.next
            pFast = pFast.next.next
        return pSlow

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)
'''
假设快指针的移动步长为2，慢指针的移动步长为1，两者同时从一个链表的起点出发向前移动，则当两个指针可以相遇时，该链表存在环链。原理很简单，从同一起点出发朝着相同方向（假设只有一条路径）的两个速度不同的物体，以慢的物体为参考系，两者存在速度差，因此慢的永远无法追上快的，除非路径中存在循环使得快的一方不断在绕圈子。当两者都进入到了环中，从参考系的角度来解释，快的一方最终会“追上”慢的一方，即最终两者必定会相遇。

当快慢指针相遇时，将快指针（或重新设定一个指针）指向链表的起点，且步长与慢指针一样为1，则慢指针与“新”指针相遇的地方就是环的入口。证明这一结论牵涉到数论的知识，这里略，
--------------------- 
作者：___Blue_H 
来源：CSDN 
原文：https://blog.csdn.net/qq_37653144/article/details/80574884 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''


'''
链接：https://www.nowcoder.com/questionTerminal/253d2c59ec3e4bc68da16833f79a38e4
来源：牛客网
华科平凡
'''

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow,fast=pHead,pHead
        while fast and fast.next:
            #下面这两行一直持续，循环，知道两个相遇
            slow=slow.next
            fast=fast.next.next
            #当快慢指针相遇时，再搞一个指针从头开始走，当这个指针与慢指针相遇时，他俩一定在入口处
            if slow==fast:
                slow2=pHead
                while slow!=slow2:
                    slow=slow.next
                    slow2=slow2.next
                return slow  #return slow2也可以