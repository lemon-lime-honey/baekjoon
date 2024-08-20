import sys
input = sys.stdin.readline

result = list()

while True:
    ipt = list(map(int, input().split()))
    if ipt[0] == 0:
        break

    stack = list()
    res = 0

    for i in range(1, ipt[0] + 1):
        while stack and ipt[stack[-1]] > ipt[i]:
            height = ipt[stack.pop()]
            width = i - 1 if not stack else i - stack[-1] - 1
            res = max(res, height * width)
        stack.append(i)

    while stack:
        height = ipt[stack.pop()]
        width = ipt[0] if not stack else ipt[0] - stack[-1]
        res = max(res, height * width)

    result.append(res)

print(*result, sep='\n')
