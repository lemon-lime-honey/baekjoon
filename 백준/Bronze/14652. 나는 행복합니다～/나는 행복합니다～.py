num = list(map(int, input().split()))
res = list()
res.append(num[2] // num[1])
res.append(num[2] % num[1])

print(' '.join(map(str, res)))