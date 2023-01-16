t = int(input())

for i in range(t):
    origin = list(map(str, input()))
    total = str(int(''.join(origin)) + int(''.join(origin[::-1])))
    if total == total[::-1]:
        print('YES')
    else:
        print('NO')