p, n = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
result = 0

for acc in a:
    if p >= 200:
        break
    p += acc
    result += 1

print(result)
