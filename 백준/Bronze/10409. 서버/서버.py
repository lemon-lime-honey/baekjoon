n, t = map(int, input().split())
time = list(map(int, input().split()))

result, total = 0, 0

for num in time:
    total += num
    if total <= t:
        result += 1
    else:
        break

print(result)