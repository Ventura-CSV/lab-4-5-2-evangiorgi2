import random


def main():
    total = 0
    i = 0
    numbers = []
    while (total <= 100):
        numbers [i] = random.randint(0, 100)
        total = sum(numbers)


    print(f'The random values are {numbers}')
    print(f'The total is {total}')


    return numbers, total


if __name__ == '__main__':
    main()
