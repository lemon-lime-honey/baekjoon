import sys
input = sys.stdin.readline


def backtrack(idx):
    global result

    if len(visited) == n // 2:
        a, b = 0, 0

        for i in range(n):
            for j in range(n):
                if i in visited and j in visited:
                    a += people[i][j]
                elif i not in visited and j not in visited:
                    b += people[i][j]

        result = min(result, abs(a - b))
        return

    for i in range(idx, n):
        if i not in visited:
            visited.add(i)
            backtrack(i + 1)
            visited.remove(i)


n = int(input())
people = [list(map(int, input().split())) for i in range(n)]
visited = set()
result = int(1e9)
backtrack(0)

print(result)