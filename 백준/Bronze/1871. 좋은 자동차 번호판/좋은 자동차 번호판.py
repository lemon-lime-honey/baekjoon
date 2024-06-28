import sys
input = sys.stdin.readline

n = int(input())
result = list()

for i in range(n):
    ipt = input().split('-')
    f = 0
    for j in range(len(ipt[0])):
        f += (ord(ipt[0][j]) - ord('A')) * 26 ** (len(ipt[0]) - j - 1)
    if abs(f - int(ipt[1])) <= 100:
        result.append('nice')
    else:
        result.append('not nice')

print(*result, sep='\n')
