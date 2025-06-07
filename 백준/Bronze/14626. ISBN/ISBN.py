num = list(input())
target = num.index("*")

for i in range(10):
    total = 0
    num[target] = str(i)
    for j in range(13):
        if j % 2:
            total += int(num[j]) * 3
        else:
            total += int(num[j])
    if total % 10 == 0:
        print(i)
        break
