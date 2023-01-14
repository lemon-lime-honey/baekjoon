n = int(input())

for i in range(1, n):
    total = i
    temp = i

    while temp > 0:
        total += (temp % 10)
        temp = temp // 10
    if total == n:
        print(i)
        break
else:
    print(0)