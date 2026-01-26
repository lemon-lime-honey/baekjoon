n, m = map(int, input().split())
score = list(map(int, input().split()))

result = [-1, 0]

for i in range(m):
    ipt = input().split()
    num = 0
    for j in range(1, n + 1):
        if ipt[j] == "O":
            num += score[j - 1]
    if result[0] < num:
        result = [num, int(ipt[0])]
    elif result[0] == num and int(ipt[0]) < result[1]:
        result[1] = int(ipt[0])

print(result[1], result[0])
