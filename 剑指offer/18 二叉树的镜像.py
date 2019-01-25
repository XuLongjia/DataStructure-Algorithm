'''
题目：操作给定的二叉树，将其变换为源二叉树的镜像。
'''

'''
剑指offer157页
29ms
5492k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return  #终止条件
        root.left,root.right = root.right,root.left  #tuple中的元素互换
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


