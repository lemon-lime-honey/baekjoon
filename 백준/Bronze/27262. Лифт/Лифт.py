n, k, a, b = map(int, input().split())
elevator = (k + n - 2) * b
stair = (n - 1)* a
print(f'{elevator} {stair}')