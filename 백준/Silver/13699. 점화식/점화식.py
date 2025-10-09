n = int(input())

t = [1]

for i in range(1, n + 1):
    target = 0
    for j in range(i):
        target += t[j] * t[i - j - 1]
    t.append(target)

print(t[-1])
