def main(): 
    container = [];
    while(True):
        value_input = input('Digite qualquer coisa (Qualquer número negativo para fechar): ');
        container.append(value_input);
        try:
            value_aux = int(container[-1]);
            if(value_aux < 0): 
                print(container);
                break;
            else: print(container);
        except: print(container);

main();