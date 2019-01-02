#!usr/bin/python
# -*- coding:utf-8 -*-
'''
1、递归是指调用自己的函数
2、每个递归函数都有两个条件，基线条件和递归条件
3、栈stack 有两种操作： push 和 pop
4、所有函数调用都进入调用栈
5、调用栈可能很长，这将占用大量的内存
'''

def fact(n):
	if n ==1:
		return 1
	else:
		return n* fact(n-1)

def countdown(n):
	print(n)
	if n <= 1:
		return
	else:
		countdown(n-1)

def main():
	print(countdown(5))

if __name__ == '__main__':
	main()