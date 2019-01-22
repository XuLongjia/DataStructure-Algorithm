'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
这一题还是挺难的，有两个栈stackA、stackB，A是入栈的，B是出栈的，入栈时，直接进入A即可，出栈时，先判断是否有元素，
如果B没有元素，pop肯定报错，应该先将A中所有的元素压倒B里面，再pop最上面一个元素，如果B中有就直接pop出，就可以，
这是最优的思路，两个栈实现了先进后出，在一起又实现了队列的先进先出。
23ms
5628k
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []  #用于入栈
        self.stackB = []  #用于出栈
        #stackA和stackB只能使用append()和pop()操作，pop()里面不能加索引

    def push(self, node):
        # write code here
        self.stackA.append(node)  #入栈，即入队

    def pop(self):
        # return xx
        if self.stackB:   #空列表为False，有元素为True
            return self.stackB.pop()
        elif not self.stackA:  #如果stackB中没有元素而且stackA中咩有元素，直接return None
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

