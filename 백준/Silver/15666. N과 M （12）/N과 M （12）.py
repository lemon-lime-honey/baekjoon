def arr(offset):
    if len(target) == m:
        result.add(tuple(target))
        return
    for i in range(offset, n):
        target.append(number[i])
        arr(i)
        target.pop()


n, m = map(int, input().split())
number = sorted(list(map(int, input().split())))
target = list()
result = set()

arr(0)
for num in sorted(result):
    print(*num)