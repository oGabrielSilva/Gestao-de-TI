def main():
    quest_est = ['primavera', 'verão', 'outono'];
    print('a)', len(quest_est));
    print('b) Inverno adicionado a lista.');
    quest_est.append('inverno');
    for x in quest_est:
        if x == 'verão': print('c)', quest_est.index(x));
main();