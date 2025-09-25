n, k = map(int, input().split())
cnt = list(map(int, input().split()))
num = [0, 0, 0, 2, 2, 3, 3, 4, 4]

for c in cnt:
    n -= num[c]

print("YES" if n <= 0 else "NO")
