#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''
二分查找，1、时间复杂度为log(n)   2、输入的list 必须为有序的，从小到大排列的
'''

def binary_search(ls,item):
	low = 0
	high = len(ls)-1

	while low <= high:   #循环条件：元素没有缩小到一个元素
		mid = int((low + high)/2)   #向下取整数，其实无所谓
		guess = ls[mid]
		if guess == item:
			return mid   #返回的是item的索引
		elif guess > item:
			high = mid-1
		else:
			low = mid +1
	return None


def main():
	ls = [1,3,4,5,8,9,11,14,36,79,90,91]
	item = 36
	print(binary_search(ls,item))

if __name__ == '__main__':
	main()



