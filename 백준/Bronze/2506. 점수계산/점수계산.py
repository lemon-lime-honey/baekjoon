n = int(input())
score = list(map(int, input().split()))
cnt = 0
total = 0

for num in score:
    if num == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0

print(total)