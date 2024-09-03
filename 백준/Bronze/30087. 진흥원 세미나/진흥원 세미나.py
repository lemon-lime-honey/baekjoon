rooms = {
    "Algorithm": 204,
    "DataAnalysis": 207,
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": 303,
    "Startup": 501,
    "TestStrategy": 105
}

n = int(input())
result = list()

for i in range(n):
    result.append(rooms[input()])

print(*result, sep="\n")
