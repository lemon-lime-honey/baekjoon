t = int(input())

for i in range(t):
    n = int(input())
    v = 0
    dist = 0

    for j in range(n):
        command = list(map(int, input().split()))
        if command[0] == 1:
            v += command[1]
        elif command[0] == 2:
            if command[1] >= v:
                v = 0
            else:
                v -= command[1]
        dist += v

    print(f'#{i + 1} {dist}')