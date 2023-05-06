n = int(input())
result = 0

for i in range(n):
    students, apple = map(int, input().split())
    result += apple % students

print(result)