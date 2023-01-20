t = int(input())

for i in range(t):
    n = int(input())
    number = list(map(int, input().split()))
    number.sort()
    print(f'#{i + 1}', end = ' ')
    print(*number)