#!usr/bin/python
# -*- coding:utf-8 -*-

'''
广度优先搜索： BFS : breadth-first search
BFS回答两类问题：1、从节点A出发，有到节点B的路径吗？  2、从节点A到节点B哪条路径最短？
BFS:一度关系大于二度关系
使用队列很容易实现BFS
队列：先入先出 First in First out FIFO  操作：出队和入队
'''

from collections import deque  #deque是一个双向队列，两头都可以pop和push

def person_is_seller(name):
	return name[-1] == 'm'    #如果最后一个字母是m 返回True，表示他是芒果经销商

def bfs(graph,name):
	search_que = deque()
	search_que += graph[name]
	while search_que:
		person = search_que.popleft()   #弹出左边的第一个item
		if person_is_seller(person):
			print(person + ' is a mango seller!')
			return True 
		else:
			search_que += graph[person]
	return False


def main():
	graph = {}
	graph['you'] = ['alice','bob','claire']
	graph['bob'] = ['anuj','peggy']
	graph['alice'] = ['peggy']
	graph['claire'] = ['thom','jonny']
	graph['anuj'] = []
	graph['peggy'] = []
	graph['thom'] = []
	graph['jonny'] = []
	print(bfs(graph,'you'))

if __name__ == '__main__':
	main()

'''
运行时间：O(V+E)  V是顶点数，E是边数
小结：
1、广度优先搜索指出是由有从A到B的路径
2、如果有，bfs将找出最短路径
3、面临类似与寻找最短路的问题时，可尝试使用图来建立模型，再使用bfs解决
4、区别有向图和无向图  directed graph and undirected graph
5、队列是FIFO，栈是LIFO
6、搜索列表必须是队列，否则找到的就不是最短路径】
7、对于检查过的人，不必再去检查，否则陷入无限循环
'''
