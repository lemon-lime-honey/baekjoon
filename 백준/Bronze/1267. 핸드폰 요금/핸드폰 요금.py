from math import ceil

n = int(input())
call = list(map(int, input().split()))

caseY = 0
caseM = 0

for tel in call:
    caseY += ceil((tel + 1) / 30) * 10
    caseM += ceil((tel + 1) / 60) * 15

if caseY < caseM:
    print(f'Y {caseY}')
elif caseY == caseM:
    print(f'Y M {caseY}')
else:
    print(f'M {caseM}')