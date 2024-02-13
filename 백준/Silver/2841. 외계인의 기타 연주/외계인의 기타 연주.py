import sys
input = sys.stdin.readline

n, p = map(int, input().split())
stack = [[] for i in range(7)]
result = 0

for i in range(n):
    nn, pp = map(int, input().split())

    while stack[nn] and stack[nn][-1] > pp:
        stack[nn].pop()
        result += 1

    if not stack[nn] or stack[nn][-1] < pp:
        stack[nn].append(pp)
        result += 1

print(result)