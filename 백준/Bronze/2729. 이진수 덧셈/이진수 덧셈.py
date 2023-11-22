t = int(input())

for i in range(t):
    n, m = input().split()
    result = int(n, 2) + int(m, 2)
    print(f'{result:b}')