#!usr/bin/python
# -*- coding:utf-8 -*-

'''
对于NP完全问题
使用近似求解算法，贪婪算法是个很常用的近似求解算法，可以得到非常接近的解

'''

def greedy(states_needed,stations):
	final_stations = set()  #存储最终结果
	while states_needed: #当仍然有没被覆盖的州时，继续迭代
		best_station = None  #每次迭代选出最优的stations
		states_covered = set()  #每次覆盖掉的州
		for station,states_for_stations in stations.items():  #stations和states
			covered = states_needed & states_for_stations   #计算交集
			if len(covered) > len(states_covered):
				best_station = station
				states_covered = covered 
		states_needed -= states_covered   #states_needed 这个集合删掉已经覆盖掉的州
		final_stations.add(best_station)  #把本次迭代选中的电台添加进去
	return final_stations


def main():
	states_needed = set(['mt','wa','or','id','nv','ut'])
	stations = {}
	stations['kone'] = set(['id','nv','ut'])
	stations['ktwo'] = set(['wa','id','mt'])
	stations['kthree'] = set(['or','nv','ca'])
	stations['kfour'] = set(['nv','ut'])
	stations['kfive'] = set(['ca','az'])

	print(greedy(states_needed,stations))

if __name__ == '__main__':
	main()