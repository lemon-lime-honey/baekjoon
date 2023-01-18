t = int(input())
contestant = list(map(int, input().split()))
cnt = 0

for num in contestant:
    if num == t:
        cnt += 1

print(cnt)