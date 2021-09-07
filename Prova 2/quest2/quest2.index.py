def main():
    print('Diga seu nome e lhe direi suas iniciais.\n');
    name = input('Seu nome: ');
    name_aux = name.split(' ');
    for name in name_aux: print(str(name[0]));
main();