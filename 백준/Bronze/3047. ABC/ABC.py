ipt = list(map(int, input().split()))
abc = input()

ipt.sort()
result = list()

for letter in abc:
    match letter:
        case "A":
            result.append(ipt[0])
        case "B":
            result.append(ipt[1])
        case "C":
            result.append(ipt[2])

print(*result)
