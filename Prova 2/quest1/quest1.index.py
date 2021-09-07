def main():
    print('CTRL + C para sair\n\nDigite um número e lhe direi se é positivo/neutro ou negativo');
    try:
        while True:
            num = int(input('Número: '));
            if num > 0: print('\nNúmero positivo\n');
            elif num < 0: print('\nNúmero negativo\n');
            elif num == 0: print('\nNúmero neutro\n');
    except: print('Fim do programa, deveria digitar um número. :c');
main();