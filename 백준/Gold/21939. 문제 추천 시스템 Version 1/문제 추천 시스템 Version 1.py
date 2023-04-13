import heapq, sys
input = sys.stdin.readline

n = int(input())
problems = dict()
easy = list()
hard = list()

for i in range(n):
    p, l = map(int, input().split())
    heapq.heappush(easy, (l, p))
    heapq.heappush(hard, (-1 * l, -1 * p))
    problems[p] = l

m = int(input())

for i in range(m):
    command = list(input().split())
    if command[0] == 'add':
        heapq.heappush(easy, (int(command[2]), int(command[1])))
        heapq.heappush(hard, (-1 * int(command[2]), -1 * int(command[1])))
        problems[int(command[1])] = int(command[2])
    elif command[0] == 'solved':
        problems[int(command[1])] = 0
    else:
        if command[1] == '1':
            while hard and problems[-1 * hard[0][1]] != -1 * hard[0][0]:
                heapq.heappop(hard)
            print(-1 * hard[0][1])
        else:
            while easy and problems[easy[0][1]] != easy[0][0]:
                heapq.heappop(easy)
            print(easy[0][1])