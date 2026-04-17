x = int(input())

for i in range(1, 9999 - x + 1):
    x += 1
    if x == (x // 100 + x % 100) ** 2:
        print(x)
        break
else:
    print(-1)
