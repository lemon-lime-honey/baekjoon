n, k = map(int, input().split())
result = 0

for i in range(n + 1):
    for j in range(60):
        for l in range(60):
            time = f'{str(i).rjust(2, "0")}' + \
                   f'{str(j).rjust(2, "0")}' + \
                   f'{str(l).rjust(2, "0")}'
            if str(k) in time: result += 1

print(result)