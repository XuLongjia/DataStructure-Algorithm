'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

'''
思路超神：
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，变成了：
4 5 6 
7 8 9
此时matrix = [[4,5,6],[7,8,9]]
思路：先进行转置，然后[].reverse()

再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可

38ms
5652k
'''

#-*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []  #存放结果
        while matrix:  #当matrix不为空时一直循环
            result += matrix.pop(0)  #每次拿出matrix的第一个元素，也就是第一行
            if matrix:
                break
            #matrix = self.turn(matrix)  #进行旋转
            matrix = [[i[j] for i in matrix] for j in range(len(matrix[0]))]
            matrix.reverse()  #这里要注意！！
        return result



