import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(p):
    global result
    chk[p] = True
    arr.append(p)

    if chk[students[p]]:
        if students[p] in arr:
            result += arr[arr.index(students[p]):]
        return
    else:
        dfs(students[p])


t = int(input())

for i in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    chk = [False for i in range(n + 1)]
    result = list()

    for j in range(1, n + 1):
        if not chk[j]:
            arr = list()
            dfs(j)

    print(n - len(result))