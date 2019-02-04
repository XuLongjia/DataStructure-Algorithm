'''
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

'''
将输入数组转成字符串，利用sort中的cmp参数对元素m和n 进行 mn or nm的比较,不过python3中没有cmp参数了
28 ms 5856k
'''

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None or numbers == []:
            return ''  #返回一个空字符串

        numbers = list(map(str, numbers))  #全部变成
        # 两两元素两种结合方式的比较，升序比较，相当于冒泡了(n*n)
        numbers.sort(cmp=lambda x, y: int(x+y) - int(y+x))   #如果为正，不交换
        t = sorted(numbers,)

        #下面两行是为了把前面的0给去掉，其实不加这段也可以AC
        while numbers[0] == '0':
            numbers.pop(0)

        return ''.join(numbers)

a = Solution()
print(a.PrintMinNumber(['3','32','321']))
