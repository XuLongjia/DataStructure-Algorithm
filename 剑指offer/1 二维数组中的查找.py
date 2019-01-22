'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
方法一： 暴力查找
284ms
5760k
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return
        row = len(array)
        col = len(array[0])

        for i in range(row):
            for j in range(col):
                if target == array[i][j]:
                    return True

        return False

'''
方法二：上述方法的时间复杂度是O(n^2)，最优化的方式是从左下或者右上开始搜索
从右上开始搜索，如果数组中的数比该数要大，那么想左移动一位，如果数组中的数比该数小，向下移动一位，
因为数组本身是从左到右依次增大，从上到下一次增大
281ms
5644k
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        raw = len(array)  #行数
        col = len(array[0])  #列数
        #从右上角开始，索引应该是array[0][col-1]
        i = 0  
        j = col - 1
        # i < raw表示 还没走到最后一行， j>=0 表示还没走到第一列
        while i < raw and j >= 0:
            if array[i][j] > target:
                #比目标大了就左移
                j -= 1
            elif array[i][j] < target:
                #比目标小了就下移
                i += 1
            else:
                return True
        return False
