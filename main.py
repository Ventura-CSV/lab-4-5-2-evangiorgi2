import random


def main():
    total = 0
    numbers = []
    randnum =0 
    temptotal=0
    while (total < 100):
        randnum = random.randint(0,99)  
        numbers.append(randnum)
        if (temptotal+randnum > 100):
            print(total, end='')
            break
        else:
            
            total = sum(numbers)
            temptotal=total

    print(f'The random values are {numbers}')
    print(f'The total is {total}')


    return numbers, total


if __name__ == '__main__':
    main()
