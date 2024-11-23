import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = list(input().rstrip())
result = list()

for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        cnt = 1
        for j in range(b, c):
            if s[j] != s[j - 1]:
                cnt += 1
        result.append(cnt)
    elif a == 2:
        for j in range(b - 1, c):
            if s[j] != "Z":
                s[j] = chr(ord(s[j]) + 1)
            else:
                s[j] = "A"

print(*result, sep="\n")
