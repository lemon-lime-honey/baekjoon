scores = list()

for i in range(8):

    scores.append((int(input()), i + 1))

scores.sort(key=lambda x:-x[0])
result = scores[:5]
result.sort(key=lambda x: x[1])

total = sum([x[0] for x in result])

print(total)
print(*[x[1] for x in result])