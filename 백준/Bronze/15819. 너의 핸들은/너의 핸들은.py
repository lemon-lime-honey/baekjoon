n, i = map(int, input().split())
handles = sorted([input() for i in range(n)])

print(handles[i - 1])
