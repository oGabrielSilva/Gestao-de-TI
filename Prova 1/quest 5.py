print('[CTRL + C para sair]')
while True:
	name = input('\nDigite seu nome:\n')
	city = input('Digite o nome da sua cidade:\n')
	datas = [
		input('Digite o dia que você nasceu (exemplo: "04"):\n'),
		input('Agora, digite o mês do seu nascimento (exemplo: "01"):\n'),
		input('E, por fim, digite o ano em que você nasceu (exemplo: "2000"):\n')
	]
	print('\nCliente:', name, '\nMora em:', city, '\nData de nascimento:', '/'.join(datas))
