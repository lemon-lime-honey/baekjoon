import heapq, sys
input = sys.stdin.readline

n = int(input())
students = list()

for i in range(n):
    heapq.heappush(students, float(input()))

for i in range(7):
    print(f'{heapq.heappop(students):.3f}')