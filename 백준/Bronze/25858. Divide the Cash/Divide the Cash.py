n, d = map(int, input().split())
solved = list()

for i in range(n):
    solved.append(int(input()))

for i in range(n):
    print(d * solved[i] // sum(solved))