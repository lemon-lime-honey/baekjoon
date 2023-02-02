t = int(input())

for i in range(t):
    n = int(input())
    one = [[0 for j in range(n)]for k in range(n)]
    two = [[0 for j in range(n)]for k in range(n)]
    three = [[0 for j in range(n)]for k in range(n)]
    number = [[0 for j in range(n)]for k in range(n)]

    for j in range(n):
        number[j] = list(map(int, input().split()))
    
    for j in range(n):
        for k in range(n):
            one[j][k] = number[n - k - 1][j]
            two[j][k] = number[n - j - 1][n - k - 1]
            three[j][k] = number[k][n - j - 1]

    print(f'#{i + 1}')

    for i in range(n):
        print(*one[i], sep = '', end = ' ')
        print(*two[i], sep = '', end = ' ')
        print(*three[i], sep = '')