ignore = {"i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"}
ipt = input().split()
result = list()

result.append(ipt[0][0].upper())

for i in range(1, len(ipt)):
    if ipt[i] in ignore:
        continue
    result.append(ipt[i][0].upper())

print("".join(result))
