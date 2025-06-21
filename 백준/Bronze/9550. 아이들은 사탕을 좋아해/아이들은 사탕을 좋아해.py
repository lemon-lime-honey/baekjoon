t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    result = 0

    for c in candy:
        if c >= k:
            result += c // k

    print(result)