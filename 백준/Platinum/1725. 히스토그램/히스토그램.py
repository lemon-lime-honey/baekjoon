import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for i in range(n)]
stack = list()
result = 0

for i in range(n):
    while stack and graph[stack[-1]] > graph[i]:
        height = graph[stack.pop()]
        width = i if not stack else i - stack[-1] - 1
        result = max(result, width * height)
    stack.append(i)

while stack:
    height = graph[stack.pop()]
    width = n if not stack else n - stack[-1] - 1
    result = max(result, width * height)

print(result)
