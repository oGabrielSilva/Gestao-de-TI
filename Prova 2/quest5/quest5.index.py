def main():
    const_list = [];
    while (len(const_list) < 3):
        const_list.append(input('Digite qualquer coisa: '));
    const_aux = input('Digite algo e veremos se é igual ao que você digitou anteriormente: ');
    if const_aux in const_list: print('Valor encontrado');
    else: print('Valor não digitado anteriormente');
main();