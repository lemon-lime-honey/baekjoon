from sys import exit
n = int(input())
numbers = list(map(int, input().split()))

if n == 1: print('A')
elif n == 2:
    if numbers[0] != numbers[1]: print('A')
    else: print(numbers[0])
else:
    if numbers[1] - numbers[0] == 0:
        a = 0
        b = numbers[0]
    else:
        a = (numbers[2] - numbers[1]) // (numbers[1] - numbers[0])
        b = numbers[1] - (numbers[2] - numbers[1]) // (numbers[1] - numbers[0]) * numbers[0]

    for i in range(1, n - 1):
        next_number = a * numbers[i] + b
        if next_number != numbers[i + 1]:
            print('B')
            exit()

    print(a * numbers[-1] + b)