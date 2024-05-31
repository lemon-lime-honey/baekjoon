n = int(input())
weights = sorted(list(map(int, input().split())))
result = 1

for w in weights:
    if result < w: break
    result += w

print(result)