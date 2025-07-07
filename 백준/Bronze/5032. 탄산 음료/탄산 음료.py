e, f, c = map(int, input().split())
result = 0
bottle = e + f

while bottle >= c:
    result += 1
    bottle -= c
    bottle += 1

print(result)
