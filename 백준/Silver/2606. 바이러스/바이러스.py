n = int(input())
link = int(input())
checked = [True, True] + [False] * (n - 1)
linked = [[] for i in range(n + 1)]
stack = [1]
result = 0

for i in range(link):
    one, two = map(int, input().split())
    linked[one].append(two)
    linked[two].append(one)


while stack:
    now = stack.pop()

    for point in linked[now]:
        if not checked[point]:
            checked[point] = True
            stack.append(point)
            result += 1

print(result)