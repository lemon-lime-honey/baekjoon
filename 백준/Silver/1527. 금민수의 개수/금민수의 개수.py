a, b = map(int, input().split())
result = 0

for i in range(a, b + 1):
    flag = True
    while i:
        if (i % 10) not in (4, 7):
            flag = False
            break
        i //= 10
    if flag:
        result += 1

print(result)