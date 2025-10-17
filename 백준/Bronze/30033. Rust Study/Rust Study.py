n = int(input())

plan = list(map(int, input().split()))
studied = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if plan[i] <= studied[i]:
        cnt += 1

print(cnt)
