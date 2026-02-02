n = int(input())
weather = list(map(int, input().split()))

result = 0
anger = 0

for w in weather:
    if w == 0:
        anger -= 1
    else:
        anger += 1
    result += anger

print(result)
