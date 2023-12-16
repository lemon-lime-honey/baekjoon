n, m = map(int, input().split())
s = set(map(int, input().split()))
result = int(1e9)

for i in range(1, 1001):
    for j in range(i, 1001):
        for k in range(j, 1002):
            if i in s or j in s or k in s:
                continue
            result = min(result, abs(n - i * j * k))

print(result)