now = list(map(int, input().split(':')))
limit = list(map(int, input().split(':')))
result = [0, 0, 0]

for i in range(3):
    if limit[i] < now[i]:
        if i == 0:
            limit[0] += 24
        elif limit[i] < now[i]:
            result[i - 1] -= 1
            limit[i] += 60
    result[i] = limit[i] - now[i]

for i in range(2, 0, -1):
    if result[i] < 0:
        result[i] += 60
        result[i - 1] -= 1

if result[0] < 0:
    result[0] += 24

print(f'{result[0]:02}:{result[1]:02}:{result[2]:02}')