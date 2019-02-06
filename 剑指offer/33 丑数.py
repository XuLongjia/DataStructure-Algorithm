'''
题目：把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

'''
质数： 2 3 5 7 11 13 17 19 23 29等等
思路：按顺序把每个丑数放在数组中，求下一个丑数
下一个丑数必定由有数组中的某一个丑数A * 2， B * 3， C * 5 的中的最小值得来。
分析：在数组中必定有一个丑数M2， 在它之前的数 * 2 都小于当前最大丑数， 在它之后的数 * 2都大于当前最大丑数，
同样有M3, M5

notes：题目的意思应该是质数因子，因为8的因子有1,2,4,8，显然不符合要求的，但是质数只有2
29ms
5848k
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0  #关键就是这三个索引

        for i in range(1,index):
            #res[t2]*2, res[t3]*3 res[t5]*5 一定是丑数，而且下一次丑数一定是这三个中的最小者
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)
            # 每次添加完了minNum，就找下面这个三个索引
            while res[t2] * 2 <= minNum:
                t2 += 1
            while res[t3] * 3 <= minNum:
                t3 += 1
            while res[t5] * 5 <= minNum:
                t5 += 1

        return res[-1]

