a, b = map(int, input().split())
result = 1

while a != b:
    if a > b: break
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else: break
    result += 1

print(-1 if a != b else result)