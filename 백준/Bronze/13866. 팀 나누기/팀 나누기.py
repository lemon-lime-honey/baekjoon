level = list(map(int, input().split()))
level.sort()
print(abs(level[0] - level[1] - level[2] + level[3]))