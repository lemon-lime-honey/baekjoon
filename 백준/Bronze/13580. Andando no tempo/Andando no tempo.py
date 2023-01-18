num = list(map(int, input().split()))
num.sort()

if (num[0] + num[1] == num[2]) + (num[0] == num[1]) + (num[1] == num[2]):
    print('S')
else:
    print('N')