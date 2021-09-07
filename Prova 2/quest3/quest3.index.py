def main():
    print('Digite um número para ver as somas ou uma letra para multiplicações');
    var_aux = input('\nDigite: ');
    var_acum = 1;
    try:
        var_aux = float(var_aux);
        for x in range(2, 11): var_acum += x;
    except:
        for x in range(2, 11): 
            var_acum *= x;
    print(var_acum); 
while True: main();