'''
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

'''
分析，两个序列才能确定一个一棵树，所以先用先序遍历，再用字符串进行匹配是不对的，因为的树的结构你确定不了。
这一题，首先判断根节点是不是相同，不相同是一个递归，把pRoot1的左右子树一次和PRoot2进行判断
如果根节点相同，那么进入下一个函数，接着判断，左边节点的下一级和左边子树下一级是不是相同，又是一个递归。
两个递归操作
29ms
5632k
'''
'''
剑指offer 148页有详细的说明

1、首先设置标志位result = false，因为一旦匹配成功result就设为true，
剩下的代码不会执行，如果匹配不成功，默认返回false
2、递归思想，如果根节点相同则递归调用Tree1HaveTree2（），
如果根节点不相同，则判断tree1的左子树和tree2是否相同，
再判断右子树和tree2是否相同
3、注意null的条件，HasSubTree中，如果两棵树都不为空才进行判断，
DoesTree1HasTree2中，如果Tree2为空，则说明第二棵树遍历完了，即匹配成功，
tree1为空有两种情况（1）如果tree1为空&&tree2不为空说明不匹配，
（2）如果tree1为空，tree2为空，说明匹配。
29ms
5696k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        # 判断根节点
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                result = self.Tree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def Tree1HaveTree2(self, pRoot1, pRoot2):
        #判断两颗子树的结构是否相同，又是一个递归函数
        #下面两个if语句是这个递归函数的终止条件
        if pRoot2 == None:  #说明已经将B树遍历完了，则直接返回True
            return True
        if pRoot1 == None: #如果B树还没空但是A树空了，说明不匹配，直接返回False
            return False
        # 这一步不断判断下一个节点，因为是递归操作。
        if pRoot1.val != pRoot2.val:
            return False
        #只有两个值相同才会调用后面return中的递归语句
        return self.Tree1HaveTree2(pRoot1.left, pRoot2.left) and self.Tree1HaveTree2(pRoot1.right, pRoot2.right)

