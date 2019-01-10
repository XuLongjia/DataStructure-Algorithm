#!usr/bin/python
# -*- coding:utf-8 -*-

class Dequeue():
    '''双端队列'''
    def __init__(self):
        '''构造的时候可以使用顺序表，也可以使用链表'''
        self._list = []

    def add_front(self,item):
        '''往队列的头部添加一个item元素'''
        self._list.insert(0,item)

    def add_rear(self,item):
        '''从队列尾部一个元素'''
        self._list.append(item)

    def pop_front(self):
        '''头部弹出元素'''
        return self._list.pop(0)

    def pop_rear(self):
        '''尾部弹出元素'''
        return self._list.pop()

    def is_empty(self):
        '''判断一个队列是否为空'''
        return self._list == []

    def size(self):
        '''返回队列的大小'''
        return len(self._list)

if __name__ == "__main__":
    q = Dequeue()
    print(q.is_empty())
    for i in range(10):
        q.add_front(i)
    #  9 8 7 6 5 4 3 2 1 0
    for i in range(20,24):
        q.add_rear(i)
    # 9 8 7 6 5 4 3 2 1 0 20 21 22 23
    print(q.pop_front())
    print(q.pop_rear())
    print(q.is_empty())
    print(q.size())