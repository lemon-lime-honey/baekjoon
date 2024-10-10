name = input()
n = int(input())
team = sorted([input() for i in range(n)])
score, idx = 0, 0

for i in range(n):
    l = name.count("L") + team[i].count("L")
    o = name.count("O") + team[i].count("O")
    v = name.count("V") + team[i].count("V")
    e = name.count("E") + team[i].count("E")

    chk = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100

    if score < chk:
        score = chk
        idx = i

print(team[idx])