#!usr/bin/python
#-*- coding:utf-8 -*-

'''
栈，一种最常用的抽象数据类型 ADT :abstract data type
'''
class Stack():
    '''stack'''
    def __init__(self):
        self._list = []

    def push(self,item):
        '''
        添加一个新元素到栈顶
        使用list应该在尾部push和pop，此时时间复杂度为O(1)
        如果使用链表的话应该在头部push和pop，此时时间复杂度为O(1)
        '''
        return self._list.append(item)

    def pop(self):
        '''弹出栈顶元素'''
        return self._list.pop()

    def peek(self):
        '''返回栈顶元素'''
        if self._list:
            return self._list[-1]
        else:
            return None

    def is_empty(self):
        '''判断栈是否为空'''
        return self._list == []
    '''
    在Python中，那些东西是假的？
    ""  0  {}  ()  []   这五个都是False
    '''

    def size(self):
        '''返回栈的元素个数'''
        return len(self._list)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
