fee = list()
result = list()
free = [30, 0, 45]

for i in range(4):
    fee.append(int(input()))

t = int(input())

for i in range(0, 3, 2):
    if t >= free[i]:
        result.append(fee[i] + 21 * (t - free[i]) * fee[i + 1])
    else:
        result.append(fee[i])

print(result[0], result[1])