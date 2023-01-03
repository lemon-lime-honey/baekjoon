def chk(num):
    for i in range(2, num):
        if (num%i)==0:
            return 0
    return 1


n = int(input())
lst = list(map(int, input().split()))
count = 0

for i in lst:
    if (i == 1):
        continue
    elif (i == 2):
        count += 1
    else:
        count += chk(i)

print(count)
