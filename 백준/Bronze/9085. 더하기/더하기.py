t = int(input())

for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    total = 0
    for number in num:
        total += number
    print(total)