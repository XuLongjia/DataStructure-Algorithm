#!usr/bin/python
# -*- coding:utf-8 -*-

class Queue():
    '''queue'''
    def __init__(self):
        '''构造的时候可以使用顺序表，也可以使用链表'''
        self._list = []

    def enqueue(self,item):
        '''往队列中添加一个item元素'''
        self._list.append(item)
        #self._list.insert(0,item)

    def dequeue(self):
        '''从队列头部删除一个元素'''
        return self._list.pop(0)
        #self._list.pop()
        #与上面的insert(0,item)相对应，具体使用哪个应该看在实际应用中哪个操作更普遍
        #两种写法总有一个时间复杂度为O(1) 另一个时间复杂度为O(n)

    def is_empty(self):
        '''判断一个队列是否为空'''
        return self._list == []

    def size(self):
        '''返回队列的大小'''
        return len(self._list)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())