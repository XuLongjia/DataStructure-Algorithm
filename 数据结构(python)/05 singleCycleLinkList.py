#/usr/bin/python
# -*- coding:utf-8 -*-

class Node():
    '''节点'''
    def __init__(self,item):
        self.elem = item
        self.next = None

class SingleCycleLinklist():
    '''单向循环链表，此时每次循环遍历的时候cur只能走到尾节点，不能走到none啦'''
    def __init__(self,node = None):  #初始化的时候可以传入一个节点，也可以不传，默认为None
        self._head = node   #私有属性，仅内部调用 表头指向第一个节点
        if node:
            node.next = node  #如果非空，则指向自己

    def is_empty(self):
        """链表是否为空，与单向链表相同"""
        return self._head == None

    def length(self):
        """遍历整个链表"""
        # cur为游标，用来移动遍历节点 比如cur = node1，cur = node2 等等
        if self.is_empty():
            return 0
        cur = self._head
        count = 1  # 用来计数
        while cur.next != self._head:  #不能走到头，只能走到尾节点，这点与之前的普通单向链表不同
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():  #如果为空直接返回
            return
        cur = self._head  #self._head 指向第一个节点
        while cur.next != self._head:  #满足只有一个节点的情况，当然也满足多个节点
            print(cur.elem,end = ' ')
            cur = cur.next
        #退出循环，cur指向尾节点，但是尾节点元素没有打印
        print(cur.elem)

    def add(self,item):
        '''头部添加元素'''
        node = Node(item)
        if self.is_empty():  #考虑假如链表为空的特殊情况
            self._head = node
            node.next = node
            return  #或者把后面的操作放到else里面
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            #循环结束后，指向最后一个节点
            node.next = self._head
            self._head = node
            cur.next = node  #或者 cur.next = self._head

    def append(self,item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():  #考虑链表为空的情况
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = cur.next  #这两句也可以改成cur.next = node 然后node.next = self._head
            cur.next = node

    def insert(self,pos,item):
        '''pos是索引，插入节点,不涉及最后一个节点，因此与单向链表的操作方式相同'''
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
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self._head:  #头节点的情况最复杂，需要改变尾节点的指向
                    rear = self._head  #设置一个游标为rear
                    while rear.next != self._head:
                        rear = rear.next
                    #循环结束后rear指向尾节点
                    self._head = cur.next  #目前cur为头节点
                    rear.next = self._head
                else:
                    pre.next = cur.next  #把 cur指向的这个节点删掉
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾部节点，并没有进行判断，所以手工判断一下
        if cur.elem == item:  #当要删除的元素在尾节点时的特殊情况
            if cur == self._head:
                #假如链表只有一个节点,此时pre仍然为None
                self._head = None
            else:
                pre.next = cur.next  #或者pre.next = self._head

    def search(self,item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self.head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:  #循环结束后到了最后一个节点，但是没有判断，因此需要手工判断一下
            return True
        return False


if __name__ == "__main__":
    ll = SingleCycleLinklist()

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