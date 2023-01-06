total = 0
minimum = 100

for i in range(7):
    temp = int(input())
    if temp % 2 == 1:
        total += temp
        if temp < minimum:
            minimum = temp

if total != 0:
    print(total)
    print(minimum)
else: print(-1)