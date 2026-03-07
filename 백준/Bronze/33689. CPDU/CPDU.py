n = int(input())

result = 0

for i in range(n):
    name = input()
    if name[0] == "C":
        result += 1

print(result)
