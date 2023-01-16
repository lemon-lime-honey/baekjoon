n = list(map(int, input().split()))

for num in n:
    if num == 9:
        print('F')
        break
else:
    print('S')