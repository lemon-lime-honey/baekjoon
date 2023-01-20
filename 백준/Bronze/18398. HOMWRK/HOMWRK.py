t = int(input())

for i in range(t):
    n = int(input())
    for j in range(n):
        n1, n2 = map(int, input().split())
        print(f'{n1 + n2} {n1 * n2}')