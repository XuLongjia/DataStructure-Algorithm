#!usr/bin/python
# -*- coding:utf-8 -*-

'''
选择排序，时间复杂度为n的平方
1、数组的元素在一起
2、链表的元素分开了
3、数组的读取速度很快
4、链表的插入和删除速度很快
5、数组的元素类型必须一致
'''

def findSmallest(arr):
	minIndex = 0   #最小值的索引
	minValue = arr[0]   #最小值
	for i in range(1,len(arr)):
		if minValue > arr[i]:
			minIndex = i #更新索引
			minValue = arr[i]   #更新值
	return minIndex

def selectSort(arr):
	newArr = []
	for i in range(len(arr)):
		minIndex = findSmallest(arr)
		newArr.append(arr.pop(minIndex))
		#print(arr)
	return newArr

def main():
	ls = [5,2,6,8,33,5,7,86,7]
	print(selectSort(ls))

if __name__ == '__main__':
	main()

