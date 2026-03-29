n, a, b = map(int, input().split())

charm = [list(map(int, input().split())) for i in range(n)]

result = False
a -= 1
b -= 1

for i in range(n):
    if charm[i][b] > charm[a][b]:
        result = True
        break
    if charm[a][i] > charm[a][b]:
        result = True
        break

print("ANGRY" if result else "HAPPY")
