def calc(num1, num2): 
    return {
        'Soma:': num1 + num2,
        'Subtração:': num1 - num2,
        'Divisão:': num1 / num2,
        'Multiplicação:': num1 * num2,
        'Exponenciação:': [num1 ** 2, num2 ** 2, num1 ** num2],
        'RaizQ:': [num1 ** .5, num2 ** .5],
        'Módulo:': num1 % num2
    }

while True:
    numbers = [float(input('\n[Sair: crtl + c]\nDigite um número: ')), float(input('Digite um número: '))]
    operators = calc(numbers[0], numbers[1])
    for operator in operators: print(operator, operators[operator])
