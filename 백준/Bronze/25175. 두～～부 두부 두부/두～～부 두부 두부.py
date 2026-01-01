from collections import deque

n, m, k = map(int, input().split())

people = deque([i for i in range(1, n + 1)])
people.rotate(-m - k + 4)

print(people[0])
