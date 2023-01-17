while True:
    n = float(input())
    if n == 0:
        break
    result = 1 + n ** 1 + n ** 2 + n ** 3 + n ** 4
    print(f'{result:.2f}')