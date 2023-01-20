x, l, r = map(int, input().split())
min = 100000
result = 0

for i in range(l, r + 1):
    if abs(x - i) < min:
        min = abs(x - i)
        result = i

print(result)