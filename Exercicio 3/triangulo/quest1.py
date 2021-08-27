def main(): 
    try:
        a = int(input('Digite o primeiro lado do triângulo:\n'));
        b = int(input('Digite o segundo lado do triângulo:\n'));
        c = int(input('Digite o terceiro lado do triângulo:\n'));
        print('\nSeu triângulo é:', evaluate(a, b, c), '\n');
    except: return print('\nTivemos algum problema. \nVerifique se digitou algum número errado. :c\n');

def evaluate(a, b, c): 
    if(a == b and b == c): return 'Equilátero.';
    elif(a != b and a != c): return 'Escaleno.';
    else: return 'Isósceles.';
    
main();