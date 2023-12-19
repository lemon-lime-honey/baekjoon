def backtrack(total, before):
    global result
    if len(chk) == n:
        result = max(result, total)
        return
    for i in range(n):
        if i in chk: continue
        chk.add(i)
        backtrack(total + abs(a[i] - before), a[i])
        chk.discard(i)


result = 0

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    chk = {i}
    backtrack(0, a[i])

print(result)