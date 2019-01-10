#usr/bin/python
#-*-coding:utf-8 -*-

class Node():
    def __init__(self,item):
        self.elem = item
        self.next = None
        self.prev = None

class DoubleLinkList():
    '''双向链表'''
    def __init__(self,node = None):  #初始化的时候可以传入一个节点，也可以不传，默认为None
        self._head = node   #私有属性，仅内部调用 表头指向第一个节点

    def is_empty(self):
        """链表是否为空,与单链表相同"""
        return self._head is None

    def length(self):
        """遍历整个链表，与单链表相同"""
        # cur为游标，用来移动遍历节点 比如cur = node1，cur = node2 等等
        cur = self._head
        count = 0  # 用来计数
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表，与单链表相同"""
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
        if node.next:  #考虑原先是空链表的情况，只要出现node.next都要考虑一下next是否存在
            node.next.prev = node  #后一个节点指向node

    def append(self,item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self._head = node  #node.next 和 prev都默认为None
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            #循环结束后cur在尾节点处
            cur.next = node
            node.prev = cur  #node的前节点指向cur

    def insert(self,pos,item):
        '''pos是索引，插入节点'''
        if pos <0:
            self.add(item)  #索引小于0默认为头插法
        elif pos > (self.length()-1):
            self.append(item)
        else:
            count = 0
            cur = self._head  #此时不需要pre啦
            while count < pos:  #循环退出时，cur为索引的节点
                count += 1
                cur = cur.next
            #循环结束后定位到了索引处的节点
            node = Node(item)
            node.next = cur
            node.prev = cur.prev  #后面两句话答案不唯一
            cur.prev.next = node #cur节点的之前那个节点应该指向新插入的node
            cur.prev = node

    def remove(self,item):
        '''删除某个具体数据 item，'''
        cur = self._head
        while cur != None:
            if cur.elem == item:
                if cur == self._head:  #判断一下是否是头节点
                    self._head = cur.next
                    if cur.next:  #考虑只有一个节点的特殊情况，此时cur.next为空
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev  #把 cur指向的这个节点删掉
                break
            else:
                cur = cur.next

    def search(self,item):
        '''查找节点是否存在，与单向链表相同'''
        cur = self._head
        while cur != None:  #如果ur.next != None 最后一个节点没有比较！
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = DoubleLinkList()
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
