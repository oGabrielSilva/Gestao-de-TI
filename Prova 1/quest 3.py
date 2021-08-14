def calc(nums):
	if nums[0] + nums[1] > 20: return True
	else: return False

print('[CTRL + C para sair]')
while True:
	nums = [
		float(input('\n------ Digite o primeiro valor: ')),
		float(input('\n------ Digite o segundo valor: '))]
	print('\nSoma maior que 20 =', calc(nums))