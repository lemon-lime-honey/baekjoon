n = int(input())
people = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    chk = 0
    for j in range(n):
        if chk == people[i] and not result[j]:
            result[j] = i + 1
            break
        if not result[j]:
            chk += 1

print(*result)