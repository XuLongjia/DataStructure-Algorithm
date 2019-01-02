#!usr/bin/python
# -*- coding:utf-8 -*-

'''
散列表就是hash表，hash函数就是一个一对一的映射
'''
voted = {}
def checkVoted(name):
	if voted.get(name):
		print('kick them out')
	else:
		voted[name] = True
		print('let them voted')

'''
散列表是一种功能强大的数据机构，其操作速度快，还能让你以不同的方式建立数据模型
1、你可以结合散列函数和数组来创建散列表
2、使用可以最大限度减少hash冲突的hash函数
3、散列表的查找、插入和删除的速度都很快
4、散列表适合用于模拟映射关系
5、一旦填装因子超过0.7，就该调整散列表的长度
6、散列表可用于缓存数据
7、散列表非常适合用于防止重复
'''