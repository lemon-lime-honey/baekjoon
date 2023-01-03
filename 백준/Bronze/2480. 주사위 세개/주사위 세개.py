num = list(map(int, input().split()))
num.sort()

count = 1
temp = 0

if (num[0] == num[1]):
    temp = num[0]
    if (num[0] == num[2]):
        count = 3
    else:
        count = 2
elif (num[1] == num[2]):
    temp = num[1]
    count = 2
else:
    temp = num[2]

if (count == 1):
    print(temp * 100)
elif (count == 2):
    print(1000 + temp * 100)
else:
    print(10000 + temp * 1000)