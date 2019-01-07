#!usr/bin/python
# -*- coding:utf-8 -*-

def gcd(x,y):
    '''
    使用辗转相除来求出最大公约数, x和y不能为0
    '''
    r = x % y
    while r != 0:
        # print(x,y,r)
        x = y
        y = r
        r = x % y
    return y

def main():
    num1 = int(input('请输入第一个数字：'))
    num2 = int(input('请输入第二个数字：'))
    x = max(num1,num2)
    y = min(num1,num2)
    print(gcd(x,y))

if __name__ == '__main__':
    main()