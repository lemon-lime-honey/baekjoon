t = int(input())

for i in range(t):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    chk = [True] + [False for i in range(n)]
    result = 0

    for j in range(1, n + 1):
        if chk[j]:
            continue
        else:
            now = j
            chk[j] = True
            while True:
                if chk[nums[now]]:
                    break
                now = nums[now]
                chk[now] = True
            result += 1

    print(result)
