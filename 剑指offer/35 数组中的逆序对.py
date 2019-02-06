'''
题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组
中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''

'''
notes：这一题没法用python做，用python始终是超时的

思路一：很巧妙
在牛客网上运算超时，但是思想很好
例如：
            0 1 2 3
            2 1 3 4     逆序数：1
      copy  1 2 3 4
            1+0+0+0=1
'''

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        copy = [i for i in data]  #复制数据
        copy.sort()  #进行排序
        count = 0

        for i in range(len(copy)):
            #每遍历一个新元素，它的对应位置总应该是0，因此它的索引值就是逆序对的个数
            count += data.index(copy[i])  #按顺序来说这个元素应该是哪个位置？
            data.remove(copy[i])  #移除这个元素不会影响后面元素逆序对的个数，假如后面元素在它前面，则不是逆序
                                #如果在后面，那么已经统计过了，这个太巧妙了，得仔细琢磨！牛！
        return count % 10000000007

'''
思路二：这一题核心还是要用归并排序，归并排序能够有效的减少最坏时间复杂度，但是它有额外的开销，以空间换时间
归并排序，就是把原数据分成两个数组，每次取两个数组中的最小值放入一个新的数组中，直到其中一个数组全部取完

不过还是超时
'''

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if data == None or len(data) <= 0:
            return 0
        copy = [i for i in data]
        n = len(data)
        count = self.InversePairsCore(data, copy, 0, n - 1)
        return count % 10000000007

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        # i初始化为前半段最后一个数字的下标
        i = start + length
        # j初始化为后半段最后一个数字的下标
        j = end

        indexCopy = end
        count = 0
        # 对两个数组进行对比取值的过程
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        # 剩下的一个数组未取完的操作
        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count







