'''
题目：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为
3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

'''
思路：同上一题思路一样，判断条件改成了行坐标和列坐标的数位之和大于k

27ms
5728k
'''

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        markmatrix = [False] * (rows * cols)
        count = self.GetNum(threshold, rows, cols, 0, 0, markmatrix)
        return count

    def GetNum(self, threshold, rows, cols, row, col, markmatrix):
        count = 0

        if self.GetSum(threshold, rows, cols, row, col, markmatrix):
            markmatrix[row * cols + col] = True
            count = 1 + self.GetNum(threshold, rows, cols, row - 1, col, markmatrix) + \
                    self.GetNum(threshold, rows, cols, row, col - 1, markmatrix) + \
                    self.GetNum(threshold, rows, cols, row + 1, col, markmatrix) + \
                    self.GetNum(threshold, rows, cols, row, col + 1, markmatrix)
        return count

    def GetSum(self, threshold, rows, cols, row, col, markmatrix):
        if row >= 0 and row < rows and col >= 0 and col < cols and self.getDigit(row) + self.getDigit(
                col) <= threshold and not markmatrix[row * cols + col]:
            return True
        return False

    def getDigit(self, number):
        sumNum = 0
        while number > 0:
            sumNum += number % 10
            number = number // 10
        return sumNum

'''
链接：https: // www.nowcoder.com / questionTerminal / 6e5207314
b5241fb83f2329e89fdecc8
来源：牛客网
华科平凡

26ms
5724k
'''



class Solution:
    def movingCount(self, threshold, rows, cols):
        self.row, self.col = rows, cols
        self.dict = set()  #记录走了几个位置
        self.search(threshold, 0, 0)
        return len(self.dict)

    def judge(self, threshold, i, j):
        #判断一下是否满足限制条件
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold

    def search(self, threshold, i, j):
        #如果不满足限制条件或或者这个位置已经走过了就直接返回
        if not self.judge(threshold, i, j) or (i, j) in self.dict:
            return
        self.dict.add((i, j))
        #一直向下走
        if i != self.row - 1:
            self.search(threshold, i + 1, j)
        #一直向左走
        if j != self.col - 1:
            self.search(threshold, i, j + 1)