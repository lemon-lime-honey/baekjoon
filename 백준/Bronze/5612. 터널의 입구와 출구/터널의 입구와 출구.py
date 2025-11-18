n = int(input())
m = int(input())
result = m
flag = False

for i in range(n):
    a, b = map(int, input().split())
    m += a - b
    result = max(result, m)
    if m < 0:
        flag = True

print(0 if flag else result)
