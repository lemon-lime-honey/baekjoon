t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    cross_word = [[0 for j in range(n)]for l in range(n)]
    result = 0
        
    for j in range(n):
        cross_word[j] = list(map(int, input().split()))
        cnt = 0

        for l in range(n):
            if cross_word[j][l]:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1
    
    for j in range(n):
        cnt = 0
        for l in range(n):
            if cross_word[l][j]:
                cnt += 1
            else:
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1
    
    print(f'#{i + 1} {result}')