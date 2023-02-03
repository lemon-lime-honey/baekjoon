target = list(map(int, input().split()))
year = [1, 1, 1]
real = 1

while True:
    if year == target:
        print(real)
        break
    real += 1
    year[0] += 1
    year[1] += 1
    year[2] += 1
    if year[0] > 15:
        year[0] -= 15
    if year[1] > 28:
        year[1] -= 28
    if year[2] > 19:
        year[2] -= 19