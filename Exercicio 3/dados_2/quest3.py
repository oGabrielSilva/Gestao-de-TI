def main():
    try:
        name = input('Olá.\nDigite seu nome: ');
        identity = input('Agora, especifique seu sexo (M ou F): ').upper();
        user_age = input('Digite sua idade: ');
        exarnet = active_ex(identity, int(user_age));
        while (len(exarnet) < 8):
            exarnet = active_ex(identity, int(user_age));
        print(f'\nNome: {name};\nSexo: {identity.upper()};\nIdade: {user_age}; \nMilitar: {exarnet}.');
    except: print('Tivemos algum problema no processamento. :c');

def active_ex(i, a):
    if(i == 'M' and a > 18): return input('Digite o número da sua dispensa militar (pelo menos 8 digitos): ');  
    else: return 'Não requerido';

main();