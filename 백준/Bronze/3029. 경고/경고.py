start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))
result = [0, 0, 0]

if start[2] <= end[2]:
    result[2] += end[2] - start[2]
else:
    result[1] -= 1
    result[2] += 60 + end[2] - start[2]

if start[1] <= end[1]:
    result[1] += end[1] - start[1]
else:
    result[0] -= 1
    result[1] += 60 + end[1] - start[1]

if start[0] <= end[0]:
    result[0] += end[0] - start[0]
else:
    result[0] += 24 + end[0] - start[0]

if result[1] < 0:
    result[0] -= 1
    result[1] += 60
if result[0] < 0:
    result[0] += 24
if result[0] == result[1] == result[2] == 0:
    result[0] = 24

print(f'{result[0]:02d}:{result[1]:02d}:{result[2]:02d}')