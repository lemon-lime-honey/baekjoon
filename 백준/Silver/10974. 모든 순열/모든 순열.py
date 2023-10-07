def permutation():
    if len(nums) == n:
        print(*nums)
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            nums.append(i)
            permutation()
            nums.pop()
            visited[i] = False


n = int(input())
visited = [False for i in range(n + 1)]
nums = list()
permutation()