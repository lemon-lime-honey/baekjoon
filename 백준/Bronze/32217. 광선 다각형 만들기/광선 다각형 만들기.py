n = int(input())
angle = list(map(int, input().split()))

print(180 * (n - 1) - sum(angle) * 2)
