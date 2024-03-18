n, p = map(int, input().split())
seen = {n: 0}
target = n
cnt = 1

while True:
    target = n * target % p
    if target in seen:
        print(len(seen) - seen[target])
        break
    seen[target] = cnt
    cnt += 1