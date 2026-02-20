n = int(input())
x, s = map(int, input().split())
weapon = sorted(
    [list(map(int, input().split())) for i in range(n)], key=lambda x: (-x[1], x[0])
)

for c, p in weapon:
    if x < c:
        continue
    if p > s:
        print("YES")
        break
else:
    print("NO")
