#!usr/bin/python
# -*- coding:utf-8 -*-

'''
快速排序：一种优雅的排序算法  算法复杂度为 O(nlog(n))
分治算法： D&C devide and conquer algorithm
'''


def quickSort(arr):
	if len(arr) <= 1:   #如果arr有0个或者1个item时，则它已经是有序的
		return arr
	else:
		pivot = arr[0]
		small = [i for i in arr[1:] if i <= pivot]
		big = [i for i in arr[1:] if i > pivot]
		print(small,pivot,big)
		return quickSort(small) + [pivot] +quickSort(big)

def main():
	ls = [10,4,5,6,7,8,9,7,4,7,9,7,7]
	print(quickSort(ls))

if __name__ == '__main__':
	main()


'''
1、D&G 将问题逐步分解，使用D&G处理列表时，基线条件很可能是空数组或只包含一个元素的数组
2、实现快速排序时，请随机的选择用在基准值的元素，快速排序的平均时间为 O(nlog(n))
3、大O表示法中的常量有时候事关重大，这就是快速排序比合并排序快的原因所在
4、比较简单查找和二分查找时，常量几乎无关紧要，因此列表很长时，O(log(n))的速度比O(n)快得多
'''
