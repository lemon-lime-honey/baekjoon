m = int(input())
lst = [1, 0, 0]

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    lst[x], lst[y] = lst[y], lst[x]

for index, value in enumerate(lst):
    if value == 1:
        print(index + 1)
        break
else:
    print(-1)