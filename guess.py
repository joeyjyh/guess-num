import random
r = random.randint(1,100)
while True:
	num = input('請猜猜看數字: ')
	num = int(num)
	if num == r:
		print('恭喜,你猜中了!')
		break
	elif num > r:
		print('猜錯囉,猜的數字比答案還要大')
	elif num < r:
		print('猜錯囉,猜的數字比答案還要小')