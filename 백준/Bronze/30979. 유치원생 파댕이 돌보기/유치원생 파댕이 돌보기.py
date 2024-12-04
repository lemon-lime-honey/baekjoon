t = int(input())
n = int(input())
candy = list(map(int, input().split()))

if t <= sum(candy):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")