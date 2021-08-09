while True: 
	nums = [
		float(input('Digite a primeira nota:')), 
		float(input('Digite a segunda nota:')),
	]
	print('Sua nota:', (nums[0] + nums[1]) / len(nums))