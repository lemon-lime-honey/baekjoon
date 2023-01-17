x = int(input())
y = int(input())

for i in range(x, y + 1):
    if (i - x) % 60 == 0:
        print(f'All positions change in year {i}')