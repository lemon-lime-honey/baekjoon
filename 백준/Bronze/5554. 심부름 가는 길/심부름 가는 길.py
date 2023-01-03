inp = list()

for i in range(4):
    inp.append(int(input()))

sec = sum(inp) % 60
min = sum(inp) // 60

print(min)
print(sec)