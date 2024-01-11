n, k = map(int, input().split())
student = [[0, 0] for i in range(6)]
result = 0

for i in range(n):
    s, y = map(int, input().split())
    student[y - 1][s] += 1

for f, m in student:
    if f >= k:
        result += f // k
        f %= k
    if m >= k:
        result += m // k
        m %= k
    if f: result += 1
    if m: result += 1

print(result)