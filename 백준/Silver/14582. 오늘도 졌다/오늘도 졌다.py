u = list(map(int, input().split()))
s = list(map(int, input().split()))
uSum = 0
sSum = 0

for i in range(9):
    uSum += u[i]
    if uSum > sSum:
        print('Yes')
        break
    sSum += s[i]
else:
    print('No')