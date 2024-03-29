from itertools import combinations

n = int(input())
snowballs = list(map(int, input().split()))
combs = combinations(range(n), 2)
snowmen = list()
result = int(1e9)

for comb in combs:
    size = snowballs[comb[0]] + snowballs[comb[1]]
    snowmen.append((size, comb[0], comb[1]))

snowmen.sort()

for i in range(len(snowmen)):
    for j in range(i + 1, len(snowmen)):
        if (snowmen[i][1] == snowmen[j][1] or
            snowmen[i][1] == snowmen[j][2] or
            snowmen[i][2] == snowmen[j][1] or
            snowmen[i][2] == snowmen[j][2]):
            continue
        result = min(result, snowmen[j][0] - snowmen[i][0])
        break

print(result)