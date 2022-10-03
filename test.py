
debug = True
#debug = False
def sum_of_list_by_index(lis, a,b,c,d,e):
	return lis[a] + lis[b] + lis[c] + lis[d] + lis[e]
	
def main():
	# read the data from xlsx
	# iterate through every possible combination, and find which is the best and cost least amount of combat power
	# sort summed power from low to high, then compare
	sum_power_list = []
	data_sum = dict()
	sum_dict = dict()
	sum_list = []
#	my_list = [100,97, 34, 52, 23, 43]
	my_list = [1016,613 ,546 ,364 ,314 ,268 ,199 ,196 ,173 ,172 ,167 ,164 ,161 ,156 ,144 ,123 ,100]
	sum = 0
	total_power = 0
	length = len(my_list)
	for a in range(length):
		if (a+5) > length: break # end of the for loop
		for b in range(a+1, length):
			for c in range(b+1, length):
				for d in range(c+1, length):
					for e in range(d+1, length):
						if debug: print(f"nums {a} {b} {c} {d} {e}")
						# obtain a sequence of order one by one
						total_power = sum_of_list_by_index(my_list, a, b, c, d, e)
						if sum_dict.get(total_power, -1) == -1:
							sum_dict[total_power] = 1
							sum_list.append(total_power)
							data_sum[total_power] = ((a,b,c,d,e),)
						else:
							sum_dict[total_power] += 1
							data_sum[total_power] = tuple(list(data_sum.get(total_power)) ) + ((a,b,c,d,e),) # data_sum[100] = origin_data_at_100 + (new tuple) -> (old tuples, new tuple)
						sum_power_list.append(total_power)
						sum += 1
	if debug: 
		print(f"The total num of value is {sum}")
		print(f"The sum of list is {sum_power_list}")
		for i, j in data_sum.items():
			print(f"The total force is {i}, and they could be formed by {j} and the total num of j is {len(j)}")
		print(sum)

main()