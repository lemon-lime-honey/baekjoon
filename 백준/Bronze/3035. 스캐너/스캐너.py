r, c, zr, zc = map(int, input().split())
article = [input() for i in range(r)]
result = list()

for i in range(r):
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(article[i][k], end="")
        print()
