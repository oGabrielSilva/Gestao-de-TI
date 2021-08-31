# -*- coding: utf-8 -*-
def main(): 
    main_counter = [];
    while(len(main_counter) < 3):
        try:
            main_counter.append(float(input('Digite um número: ')));
            print(main_counter);
        except: 
            print('------- Digite números, por favor -------');
            continue;
    for x in range(100):
        if(x % 2 > 0): 
            if(not(x in main_counter)): print(x);
        
main();