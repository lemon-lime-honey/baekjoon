n = int(input())

result = 0
cnt = 0

votes = list(map(int, input().split()))

for vote in votes:
    if vote == 0:
        cnt += 1
        if cnt >= n / 2:
            print("INVALID")
            break
    result += vote
else:
    print("APPROVED" if result > 0 else "REJECTED")
