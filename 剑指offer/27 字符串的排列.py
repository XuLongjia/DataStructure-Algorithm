'''
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

'''
依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。
33ms
5632k
'''

# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss) #把字符串转换成列表
        charList.sort()  #按照字母的assci进行排序
        res = []  #存放结果，每个append进入的元素都是一种集合
        for i in range(len(charList)):  #字符串多长就循环多少次
            if i > 0 and charList[i] == charList[i-1]:  #连续两个字符相同进入下一次循环
                continue
            subres = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for j in subres:
                res.append(charList[i]+j)  #字符串拼接
        return res
