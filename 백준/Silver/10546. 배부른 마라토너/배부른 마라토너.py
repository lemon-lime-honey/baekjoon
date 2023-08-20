from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
name = defaultdict(int)

for i in range(n):
    name[input().rstrip()] += 1

for i in range(n - 1):
    name[input().rstrip()] -= 1

for key, value in name.items():
    if value:
        print(key)
        break