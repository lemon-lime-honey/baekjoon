import sys

surname = dict()
result = list()
n = int(sys.stdin.readline())

for i in range(n):
    temp = sys.stdin.readline()[0]
    if temp not in surname:
        surname[temp] = 1
    else:
        surname[temp] += 1

for key, value in surname.items():
    if value >= 5:
        result.append(key)

if len(result) == 0:
    print('PREDAJA')
else:
    result.sort()
    print(''.join(result))