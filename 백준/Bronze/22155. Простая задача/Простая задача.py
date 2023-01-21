n = int(input())

for i in range(n):
    i, f = map(int, input().split())
    if (i <= 1) * (f <= 2) + (i <= 2) * (f <= 1):
        print('Yes')
    else:
        print('No')