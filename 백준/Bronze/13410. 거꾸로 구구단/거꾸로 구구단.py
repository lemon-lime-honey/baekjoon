n, k = map(int, input().split())
maximum = 0

for i in range(1, k + 1):
    temp = n * i
    chk = 0
    while temp:
        chk = 10 * chk + temp % 10
        temp //= 10
    maximum = max(maximum, chk)

print(maximum)