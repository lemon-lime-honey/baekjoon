n = int(input())
tower = list(map(int, input().split()))

result = 0
last = 0

for t in tower:
    if last <= t:
        result += 1
    last = t

print(result)
