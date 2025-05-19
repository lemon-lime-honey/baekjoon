n, t = map(int, input().split())
period = list(map(int, input().split()))
result = 0

for p in period:
    num = 0
    while True:
        if t % (p + num) == 0:
            break
        if t % (p - num) == 0 and p > num:
            break
        num += 1
    result += num

print(result)
