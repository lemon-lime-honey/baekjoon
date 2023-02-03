t = int(input())

for i in range(t):
    number = list(map(int, input().split()))
    number.sort()
    print(f'#{i + 1} {(sum(number[1:9]) / 8):0.0f}')