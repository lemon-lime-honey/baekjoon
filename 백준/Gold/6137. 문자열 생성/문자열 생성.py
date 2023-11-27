from collections import deque
import sys
input = sys.stdin.readline


def compare(start, end):
    if end - start < 2:
        return s[start] < s[end]
    if s[start] == s[end]:
        return compare(start + 1, end - 1)
    return s[start] < s[end]


n = int(input())
s = deque([input().rstrip() for i in range(n)])
result = list()
idx = 0

while s:
    if s[0] != s[-1]:
        if s[0] < s[-1]:
            result.append(s.popleft())
        else:
            result.append(s.pop())
    else:
        if compare(0, len(s) - 1):
            result.append(s.popleft())
        else:
            result.append(s.pop())

while (idx < n):
    if n - idx <= 80:
        print(*result[idx:], sep='')
        break
    else:
        print(*result[idx: idx + 80], sep='', end='\n')
        idx += 80