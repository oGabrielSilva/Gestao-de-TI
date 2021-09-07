def main():
    const_inter = [];
    const_list = [[], []];
    print(len(const_list[0]) < 5);
    while ((len(const_list[0]) < 5) or (len(const_list[1]) < 5)):
        if(len(const_list[0]) < 5): 
            const_list[0].append(int(input('Digite um número: ')));
        elif(len(const_list[1]) < 5): 
            const_list[1].append(int(input('Digite um número para a segunda lista: ')));
    for x in const_list[0]: 
        if x in const_list[1]: const_inter.append(x);
    print('Intersecção: ', const_inter);
try: main();
except: print('Digite números.');
