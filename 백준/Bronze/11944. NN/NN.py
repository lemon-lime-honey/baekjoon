n, m = input().split()
m = int(m)
res = list()

for i in range(int(n)):
    res.extend(list(n))
    if len(res) > m:
        while len(res) > m:
            res.pop()
        break

print(''.join(res))