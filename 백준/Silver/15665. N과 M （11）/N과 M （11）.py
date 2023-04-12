def arr(point):
    if len(target) == m:
        result.add(tuple(target))
        return
    for i in range(n):
        target.append(number[i])
        arr(point)
        target.pop()


n, m = map(int, input().split())
number = sorted(list(map(int, input().split())))
target = list()
result = set()

arr(0)
for num in sorted(result):
    print(*num)