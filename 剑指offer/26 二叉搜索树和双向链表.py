'''
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

'''
思路：由于输入的一个二叉搜索树，其左子树大于右子树的值，这位后面的排序做了准备，因为只需要中序遍历即可，将所有
的节点保存到一个列表，。对这个list[:-1]进行遍历，每个节点的right设为下一个节点，下一个节点的left设为上一个节点。

29ms
5632k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return
        self.res = []  #存放所有节点
        self.inOrder(pRootOfTree)  #此时已经安序存放了所有节点
        for i, node in enumerate(self.res[:-1]):
            node.right = self.res[i + 1]  #每个节点的right设为下一个节点
            self.res[i + 1].left = node  #下一个节点的left设为上一个节点
        return self.res[0]

    def inOrder(self, root):
        '''二叉搜索树的中序遍历就是从小到大排序！！！'''
        if root is None:
            return  #定义递归的终止条件
        self.inOrder(root.left)
        self.res.append(root)
        self.inOrder(root.right)

