#!usr/bin/python
#-*- coding:utf-8 -*-

class Node():
    '''节点'''
    def __init__(self,item):
        self.elem = item
        self.next = None

class SingleLinklist():
    '''单向链表'''
    def __init__(self,node = None):  #初始化的时候可以传入一个节点，也可以不传，默认为None
        self._head = node   #私有属性，仅内部调用 表头指向第一个节点

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        """遍历整个链表"""
        # cur为游标，用来移动遍历节点 比如cur = node1，cur = node2 等等
        cur = self._head
        count = 0  # 用来计数
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head  #self._head 指向第一个节点
        while cur != None:
            print(cur.elem,end = ' ')
            cur = cur.next
        print('')  #换行

    def add(self,item):
        '''头部添加元素'''
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self,pos,item):
        '''pos是索引，插入节点'''
        if pos <0:
            self.add(item)  #索引小于0默认为头插法
        elif pos > (self.length()-1):
            self.append(item)
        else:
            count = 0
            pre = self._head  #pre表示索引的前一个节点
            while count < (pos-1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        '''删除某个具体数据 item'''
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                if pre == None:  #或者cur = self._head 判断一下是否是头节点
                    self._head = cur.next
                else:
                    pre.next = cur.next  #把 cur指向的这个节点删掉
                return
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        '''查找节点是否存在'''
        cur = self._head
        while cur != None:  #如果ur.next != None 最后一个节点没有比较！
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinklist()

    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 2 3 4 5 6
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3 4 5 6
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 2 3 4 5 6 200
    ll.travel()

    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()

