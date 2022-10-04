# 蒙特卡洛 方法 判断击落概率

from random import shuffle

debug = False
def judge(attack : list[int], defend : list[int]) -> int:
	# task: judge whether attack can defeat defend nums and return True or False
	
	# sub1: 判断大小是否一致 : 待完成
	total = len(attack)
	# sub2: judge whether attack coud beat defend and return result
	win = 0
	for i in range(len(attack)):
		win += (attack[i] > defend[i])
	# return example
	# win	lose -> result
	# 2  	2 -> False.
	# 3  	2 -> True
	return 1 if win > total/2 else 0

def test_cases_generator(originList : list[int]) -> list[int]:
	posNum = len(originList)-1
	for (index, testNum) in enumerate(originList):
		newList = originList[:index] + originList[index:]
		# I couldn't write it out...  ||<>..<>||
	pass
def cankill_brutal(attack : list[int], defend : list[int], testNum = 100, probability = 0.95):
	game_num = 0
	win = 0
	testCases = test_cases_generator(defend)
	for tsetCase in testCases:
		game_num += 1
		win += judge(attack, testCases)
	if win >= probability * game_num:
		return True
	else:
		return False
	
def cankill_montecarlo(attack : list[int], defend : list[int], testNum = 100, probability = 0.95, debug = False):
	if testNum <= 0: 
		if debug == True: print("Invalid test number for mentekaluo")
		return False
	
	else: # testNum > 0
		game_num = testNum
		win = 0
		for i in range(testNum):
			shuffle(defend)
			if judge(attack, defend) == 0:
				if debug:
					print(f"You loose at {attack} vs {defend}")
			else:
				win += 1
			# win += judge(attack, defend)
		if debug == True:
			print(f"\nWin time = {win}, probability of winning is {win/testNum}\n")
		if win >= probability * testNum:
			return True
		return False

#test = False
if __name__ == "__main__":
	test = True
	if test == True:
		print("can you kill", end = " ")
	#	print(canKill_mentekaluo([5,5,5,3,1], [4,4,5,3,2]))
		print(cankill_montecarlo([364, 314, 229, 100, 100], [188, 195, 243, 217, 195]))
		print(cankill_montecarlo([161, 156, 142, 123, 100], [65, 133, 106, 85, 119]))
		print(cankill_montecarlo([199, 181, 172, 172, 144], [180, 188, 171, 148, 143]))
	#	print(canKill_montecarlo([161, 156, 144, 123, 100], [135, 136, 118, 116, 103]))
	#	print(canKill_montecarlo([199, 266,167, 196, 100], [188,195,185,163,195], testNum = 20000))
	#	print(canKill_montecarlo([199, 266,167, 196, 100], [156,144,150,150,153], testNum = 20000))
	#	print(canKill_montecarlo([123, 164,156, 164, 100], [156,144,150,150,153], testNum = 20000)) # actually 0.9's probability of winning 
		print(cankill_montecarlo([364, 130,613, 546, 156], [217,238,249,267,323], testNum = 20000))
		print(cankill_montecarlo([364, 546, 613, 314, 268], [1268,1062,340,257,229], testNum= 4000, debug=True, probability=0.59))
	else:
		print("Test is not run")
	
	
