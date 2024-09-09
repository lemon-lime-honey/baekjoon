ipt = input()
n = len(ipt)
r, c = 0, 0

for i in range(int(n ** 0.5), 0, -1):
    if n % i == 0:
        r, c = i, n // i
        break

for i in range(r):
    for j in range(c):
        print(ipt[i + j * r], end='')