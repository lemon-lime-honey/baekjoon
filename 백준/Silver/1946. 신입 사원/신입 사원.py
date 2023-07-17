import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    people = [list(map(int, input().split())) for i in range(n)]

    people.sort()
    ref = people[0][1]
    result = 1

    for j in range(1, n):
        if people[j][1] < ref:
            result += 1
            ref = people[j][1]

    print(result)