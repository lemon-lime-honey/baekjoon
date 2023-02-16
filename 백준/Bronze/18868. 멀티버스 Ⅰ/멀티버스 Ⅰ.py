def compare(x, y):
    for k in range(n):
        for l in range(k, n):
            if planet[x][k] < planet[x][l]:
                if planet[y][k] >= planet[y][l]:
                    return False
            elif planet[x][k] > planet[x][l]:
                if planet[y][k] <= planet[y][l]:
                    return False
            elif planet[x][k] == planet[x][l]:
                if planet[y][k] != planet[y][l]:
                    return False
    
    return True

m, n = map(int, input().split())
planet = list()
result = 0

for i in range(m):
    planet.append(list(map(int, input().split())))

for i in range(m):
    for j in range(i + 1, m):
        if compare(i, j):
            result += 1

print(result)