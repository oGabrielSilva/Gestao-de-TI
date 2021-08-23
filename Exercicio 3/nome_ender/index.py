def main(): 
    user_name = input('Digite seu nome: ');
    user_address = input('Digite seu endereço: ');
    if(def_counter(user_name, 20)): 
        return print(f'\nOpss... {user_name} possui {len(user_name)}. Limite de 20.');   
    elif(def_counter(user_address, 30)): 
        return print(f'\nOpss... {user_address} possui {len(user_address)}. Limite de 30');
    print(f'\nNome: {user_name};\nEndereço: {user_address}.');

def def_counter(counter, val): 
    if(len(counter) > val): return True; 
    else: return False;

main()