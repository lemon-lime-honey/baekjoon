num = 0
max = 0

for i in range(1, 6):
    score = list(map(int, input().split()))
    if max < sum(score):
        num = i
        max = sum(score)

print(f'{num} {max}')