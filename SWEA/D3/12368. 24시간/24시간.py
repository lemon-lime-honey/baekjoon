tc = int(input())

for i in range(tc):
    a, b = map(int, input().split())
    print(f'#{i + 1} {(a + b) if (a + b) < 24 else (a + b - 24)}')