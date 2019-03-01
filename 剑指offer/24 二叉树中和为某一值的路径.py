'''
题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

'''
思路：
递归先序遍历树， 把结点加入路径。使用列表结构存树结构
若该结点是叶子结点则比较当前路径和是否等于期待和，叶子节点说明该路径应该截止了
弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点。

25ms
5670k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []  #存放结果

        def FindPath2(root, path, currentNum):
            currentNum += root.val
            # root使用append转成了列表，因为最后要一个序列，root本身还是树结构
            path.append(root)
            # 判断是不是到叶子节点了，到叶子节点了就要判断值的和是不是相等
            flag = root.left == None and root.right == None
            # 返回值是一个等于整数的序列
            if currentNum == expectNumber and flag:  #flag为真表示到了叶节点
                result.appned([node.val for node in path])

            if currentNum < expectNumber:
                if root.left:
                    FindPath2(root.left, path, currentNum)
                if root.right:
                    FindPath2(root.right, path, currentNum)
            # 拿到一个正确的路径后要弹出，回到上一次父节点继续递归
            path.pop()

        FindPath2(root, [], 0)
        return result

'''
链接：https: // www.nowcoder.com / questionTerminal / b736e784e3e34731af99065031301bca
来源：牛客网
华科平凡

23

'''



class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        treepath = self.dfs(root)  #所有的路径
        for i in treepath:
            path = list(map(int,i.split(",")))
            if sum(path) == expectNumber:
                res.append(path)
        return res

    #定义递归函数dfs找到所有的路径
    def dfs(self, root):
        #两个终止条件
        if not root: return []
        if not root.left and not root.right:
            return [str(root.val)]
        #下面两句是递归函数
        treePath = [str(root.val) + "," + path for path in self.dfs(root.left)]
        treePath += [str(root.val) + "," + path for path in self.dfs(root.right)]
        return treePath