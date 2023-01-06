num = list()
row = 0
column = 0
max = 0

for i in range(9):
    num = list(map(int, input().split()))
    for n in num:
        if max < n:
            max = n
            row = i + 1
            column = num.index(n) + 1
if max == 0:
    print(0)
    print('1 1')
else:
    print(max)
    print(f'{row} {column}')