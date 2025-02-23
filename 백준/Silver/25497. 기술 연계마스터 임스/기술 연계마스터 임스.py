n = int(input())
skill = input()
result = 0

seen = {"L": 0, "S": 0}

for i in range(n):
    if skill[i].isdigit():
        result += 1
    else:
        if skill[i] in "LS":
            seen[skill[i]] += 1
        else:
            if skill[i] == "R" and seen["L"]:
                seen["L"] -= 1
                result += 1
            elif skill[i] == "K" and seen["S"]:
                seen["S"] -= 1
                result += 1
            else:
                break

print(result)
