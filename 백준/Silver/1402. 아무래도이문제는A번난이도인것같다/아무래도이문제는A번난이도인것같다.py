t = int(input())

for i in range(t):
    a, b = map(int, input().split())

print(*['yes' for i in range(t)], sep="\n")