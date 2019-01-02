#usr/bin/python
# -*- coding:utf-8 -*-

'''
dijkstra算法的步骤：
1、找出最便宜的节点，即可在最短时间内到达的节点
2、更新该节点邻居的开销
3、重复以上过程
4、计算最终路径
'''
processed = []  #创建一个数组，用于记录处理过的节点

def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node


def dijkstra(graph,costs,parents):
	node = find_lowest_cost_node(costs)
	while node is not None:
		cost = costs[node]
		neighbors = graph[node]
		for n in neighbors.keys():
			if costs[n] > cost + neighbors[n]:
				costs[n] = cost + neighbors[n]
				parents[n] = node
		processed.append(node)
		node = find_lowest_cost_node(costs)
	return costs,parents


def main():
	graph = {}

	graph['start'] = {}
	graph['start']['a'] = 6
	graph['start']['b'] = 2

	graph['a'] = {}
	graph['a']['fin'] = 1

	graph['b'] = {}
	graph['b']['a'] = 3
	graph['b']['fin'] = 5

	graph['fin'] = {}

	costs = {}
	costs['a'] = 6
	costs['b'] = 2
	costs['fin'] = float('inf')

	parents = {}
	parents['a'] = 'start'
	parents['b'] = 'start'
	parents['fin'] = 'None'

	print(dijkstra(graph,costs,parents))


if __name__ == '__main__':
	main()

'''
1、广度优先搜索用于在非加权图中查找最短路径
2、dijkstra算法用于在加权图中查找最短路径
3、仅当权重为正时dijkstra算法才管用
4、如果图中包含负权边，请使用贝尔曼-福德算法
'''