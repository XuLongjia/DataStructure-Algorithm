#!usr/bin/python
# -*- coding:utf-8 -*-

def eratosthenes(n):
    '''
    使用埃拉托斯特尼筛法，打印2到n的所有质数
    '''
    isPrime = [True] * (n+1)  #设置一个bool型的数组
    isPrime[1] = False
    for i in range(2,int(n**0.5)+1):  #i用来筛选，到根号下n即可
        if isPrime[i]:  #如果i是质数，则把i的倍数全部设置为False
            for j in range(i*i,n+1,i):  #起始点设置的很讲究，最后的i表示以i为间隔
                isPrime[j] = False
    return [x for x in range(2,n+1) if isPrime[x]]

def main():
    print(eratosthenes(1000))

if __name__ == '__main__':
    main()