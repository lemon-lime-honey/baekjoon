n = int(input())
req = list(map(int, input().split()))
seat = [True] * 101
cnt = 0

for num in req:
    if seat[num]:
        seat[num] = False
    else:
        cnt += 1

print(cnt)