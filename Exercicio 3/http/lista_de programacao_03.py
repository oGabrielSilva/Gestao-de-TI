#Primeira questão
a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if((a == b) & (a == c)):
    print("É um triângulo equilátero")
elif((a != b) & (a != c)):
    print("É um triângulo escaleno")
else:
    print("É um triângulo isósceles")

#Segunda questão
nome = input("Nome: ")
nome = nome.capitalize()
sexo = input("Sexo ao nascer, 'M' para Masculino e ‘F’ para feminino: ")
sexo = sexo.capitalize()
if(sexo.startswith('M')):
    idade = input("Idade: ")
    print("Nome: ", nome)
    print("Sexo: ", sexo)
    print("Idade: ", idade)
elif(sexo.startswith("F")):
    print("Nome: ", nome)
    print("Sexo: ", sexo)

#Terceira questão
nome = input("Nome: ")
nome = nome.capitalize()
sexo = input("Sexo ao nascer, 'M' para Masculino e ‘F’ para feminino: ")
sexo = sexo.capitalize()
if(sexo.startswith('M')):
    idade = input("Idade: ")
    if(int(idade) >= 18):
        NumDispensaMilitar = input('Número da dispensa militar (pelo menos 8 digitos): ')
        while(len(NumDispensaMilitar) < 8):
            print("Número de Dispensa Militar invalido, tente novamente")  
            NumDispensaMilitar = input('Número da dispensa militar (pelo menos 8 digitos): ')
    print("Nome: ", nome)
    print("Sexo: ", sexo)
    print("Idade: ", idade)
    print("Número de Dispensa Militar: ", NumDispensaMilitar)
elif(sexo.startswith("F")):
    idade = input("Idade: ")
    print("Nome: ", nome)
    print("Sexo: ", sexo)
    print('Idade:', idade)
    print('Você não precisou se alistar.')

#Quarta questão
site = input("Insira o endereço do Site: ")
if(site.startswith('https://')):
    print('O site é seguro')
elif(site.startswith('http://')):
    print('O site não é seguro')

#Quinta questão
nome = input("Insira o nome: ")
endereco = input("Insira o endereço: ")
if(len(nome) > 20):
    print('nome inválido, máx. 20 caracteres. (Você digitou', len(nome), ')')
if(len(endereco) > 30):
    print('Endereço invalido, máx. 30 caracteres. (Você digitou', len(endereco), ")")