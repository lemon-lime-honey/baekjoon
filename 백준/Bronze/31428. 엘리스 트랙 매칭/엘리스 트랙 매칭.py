from collections import Counter

n = int(input())
cnt = Counter(input().split())

print(cnt.get(input(), 0))
