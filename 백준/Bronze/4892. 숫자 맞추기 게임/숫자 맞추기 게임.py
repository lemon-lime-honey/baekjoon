import sys
input = sys.stdin.readline

case = 1

while True:
    n = int(input())
    if not n: break
    
    result = 0
    print(f'{case}.', end=' ')

    if n % 2:
        print('odd', end=' ')
        result = (3 * n + 1) // 2
    else:
        print('even', end = ' ')
        result = 3 * n // 2

    result = result * 3 // 9
    print(result)
    case += 1