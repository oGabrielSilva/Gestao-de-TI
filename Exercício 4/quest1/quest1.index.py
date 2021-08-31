names = ['Misael', 'Charlotte', 'Artémis', 'Arthur', 'Leona'];

def main(): 
    print(f'a) Primeiro nome da lista: {names[0]};\nb) Segundo nome da lista: {names[-1]};');
    names[2] = 'Diana';
    print('c) Terceiro nome trocado para:', names[2] + ';\nd)');
    for i in range(len(names)): print(f'  {i + 1}. {names[i]};');

main();