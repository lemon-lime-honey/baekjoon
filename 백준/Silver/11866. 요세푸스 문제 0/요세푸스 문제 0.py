from collections import deque

n, k = map(int, input().split())
people = deque([x for x in range(1, n + 1)])
result = list()

while people:
    people.rotate(-k)
    result.append(people.pop())

print('<', end = '')

for i in range(n - 1):
    print(result[i], end = ', ')

print(f'{result[n - 1]}>')