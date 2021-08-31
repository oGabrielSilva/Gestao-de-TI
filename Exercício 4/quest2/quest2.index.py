def main():
    numbers = [2, 3, 8, 4, 9, 7, 1, 6, 5];
    uppers = 0;
    for number in numbers: 
        if(numbers[-1] > number): uppers += 1;
    print(uppers, 'números maiores que', numbers[-1]);

main();