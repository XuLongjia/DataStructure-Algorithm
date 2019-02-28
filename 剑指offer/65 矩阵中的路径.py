'''
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个
格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路
径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含
"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

'''
思路：优化版回溯法
1.将matrix字符串模拟映射为一个字符矩阵(但并不实际创建一个矩阵)
2.取一个boolean[matrix.length]标记某个字符是否已经被访问过,用一个布尔矩阵进行是否存在该数值的标记。
3.如果没找到结果，需要将对应的boolean标记值置回false,返回上一层进行其他分路的查找。

36ms
5697k
'''

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        # 模拟的字符矩阵
        markmatrix = [0] * (rows * cols)
        pathlength = 0
        # 从第一个开始递归，当然第一二个字符可能并不位于字符串之上，所以有这样一个双层循环找起点用的，
        # 一旦找到第一个符合的字符串，就开始进入递归，
        # 返回的第一个return Ture就直接跳出循环了。
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathlength, markmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathlength, markmatrix):
        # 说明已经找到该路径，可以返回True
        if len(path) == pathlength:
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathlength] and not \
                markmatrix[row * cols + col]:
            pathlength += 1
            markmatrix[row * cols + col] = True
            # 进行该值上下左右的递归
            hasPath = self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathlength, markmatrix)

            # 对标记矩阵进行布尔值标记
            if not hasPath:
                pathlength -= 1
                markmatrix[row * cols + col] = False
        return hasPath

'''
华科平凡的思路：

链接：https: // www.nowcoder.com / questionTerminal / c61c6999eecb4b8f88a98f66b273a3cc
来源：牛客网
29ms
5752K
'''

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, board, row, col, word):
        self.col, self.row = col, row  #先将这两个参数变成self的，下面的函数就不用传值了
        board = [list(board[col * i:col * i + col]) for i in range(row)]  #将输出的矩阵变成二维list
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    self.b = False  #先设置flag为False
                    self.search(board, word[1:], [(i, j)], i, j)  #进行递归搜索
                    if self.b:  #如果找到了就将flag设置为True
                        return True

        return False

    def search(self, board, word, bool_dict, i, j):
        if word == "":  #说明已经全部都找到了
            self.b = True
            return
        #下面四个if判断语句都需要同时满足三个条件：1、没有走到边缘，2、没有被之前的字符使用过 3、找到了下一个字符
        #往左走
        if j != 0 and (i, j - 1) not in dict and board[i][j - 1] == word[0]:
            self.search(board, word[1:], bool_dict + [(i, j - 1)], i, j - 1)
        #往上走
        if i != 0 and (i - 1, j) not in dict and board[i - 1][j] == word[0]:
            self.search(board, word[1:], bool_dict + [(i - 1, j)], i - 1, j)
        #往右走
        if j != self.col - 1 and (i, j + 1) not in dict and board[i][j + 1] == word[0]:
            self.search(board, word[1:], bool_dict + [(i, j + 1)], i, j + 1)
        #往下走
        if i != self.row - 1 and (i + 1, j) not in dict and board[i + 1][j] == word[0]:
            self.search(board, word[1:], bool_dict + [(i + 1, j)], i + 1, j)