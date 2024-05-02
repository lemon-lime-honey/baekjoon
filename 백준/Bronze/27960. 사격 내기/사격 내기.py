sa, sb = map(int, input().split())
score = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
result = 0

for s in score:
    if sa & s and sb & s or not sa & s and not sb & s:
        continue
    result += s

print(result)