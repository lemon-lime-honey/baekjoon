tc = int(input())

for i in range(tc):
    l, u, x = map(int, input().split())
    if x <= l:
        print(f'#{i + 1} {l - x}')
    elif x <= u:
        print(f'#{i + 1} 0')
    else:
        print(f'#{i + 1} -1')