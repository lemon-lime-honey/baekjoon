from collections import deque

n, k  = map(int, input().split())
number = deque(range(1, n + 1))

print('<', end = '')

while len(number) > 1:
    number.rotate(-k)
    print(f'{number.pop()}, ', end ='')

print(f'{number.pop()}>')