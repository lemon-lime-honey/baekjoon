k = int(input())
s = input()

result = list()

for i in range(0, len(s), k):
    result.append(s[i])

print("".join(result))
