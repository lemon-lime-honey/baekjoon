n, k = map(int, input().split())
a = list(map(int, input().split()))
s = 1
num = 0

for i in range(n):
    if a[i] | k != k:
        num = 0
        s = i + 2
    else:
        num |= a[i]
        if num == k:
            print(s, i + 1)
            break
else:
    print(-1)
