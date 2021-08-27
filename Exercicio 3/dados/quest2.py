def main():
    name = input('Olá.\nDigite seu nome: ');
    identity = input('Agora, especifique seu sexo (M ou F): ');
    user_age = active_ua(identity.upper());
    print(f'\nNome: {name};\nSexo: {identity.upper()};\nIdade: {user_age}.');

def active_ua(i):
    if(i == 'M'): return input('Digite sua idade: ');
    elif(i == 'F'): return 'Not required';
    else: return 'Err';

main();