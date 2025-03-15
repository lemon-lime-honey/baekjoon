n = int(input())
hor = [input() for i in range(n)]

for i in range(n):
    temp = list()
    for j in range(n):
        temp.append(hor[j][i])
    if hor[i] != "".join(temp):
        print("NO")
        break
else:
    print("YES")
