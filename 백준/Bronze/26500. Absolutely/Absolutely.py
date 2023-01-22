n = int(input())

for i in range(n):
    number = list(map(float, input().split()))
    print(f'{abs(number[1] - number[0]):.1f}')