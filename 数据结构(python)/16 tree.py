#!usr/bin/python
# -*- coding:utf-8 -*-

class Node():
    '''节点类'''
    def __init__(self,item=-1,lchild = None, rchild = None):
        self.elem = item
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    '''二叉树'''
    def __init__(self,Node = None):
        self.root = Node

    def add(self,elem):
        '''按照层次遍历的顺序给树添加节点'''
        node = Node(elem)
        #如果根节点是空的，就给根节点赋值
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.elem,end=' ')
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild !=None:
                queue.append(node.rchild)
        print('')

    def preOrder(self,node):
        '''先序遍历，根、左、右'''
        '''递归实现'''
        if node is None:
            return
        print(node.elem,end = ' ')
        self.preOrder(node.lchild)
        self.preOrder(node.rchild)

    def inOrder(self,node):
        '''中序遍历，左、根、右'''
        '''递归实现'''
        if node is None:
            return
        self.inOrder(node.lchild)
        print(node.elem,end= ' ')
        self.inOrder(node.rchild)

    def postOrder(self,node):
        '''后序遍历，左右根'''
        '''递归实现'''
        if node is None:
            return
        self.postOrder(node.lchild)
        self.postOrder(node.rchild)
        print(node.elem,end=' ')

if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    print('层次遍历：',end = ' ')
    tree.breadth_travel()
    print('先序遍历：',end = ' ')
    tree.preOrder(tree.root)
    print('')
    print('中序遍历：', end=' ')
    tree.inOrder(tree.root)
    print(' ')
    print('后序遍历：', end=' ')
    tree.postOrder(tree.root)
    print(' ')

