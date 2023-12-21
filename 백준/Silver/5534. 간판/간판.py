def backtrack(idx, name_idx):
    global result
    if len(chk) == len(name):
        indices = sorted(list(chk))
        for i in range(1, len(indices) - 1):
            if (indices[i] - indices[i - 1]) != (indices[i + 1] - indices[i]):
                return False
        result += 1
        return True

    for i in range(idx, len(material)):
        if i in chk or material[i] != name[name_idx]:
            continue
        chk.add(i)
        if backtrack(i + 1, name_idx + 1): return True
        chk.discard(i)

    return False


n = int(input())
name = input()
materials = [input() for i in range(n)]
result = 0

for material in materials:
    chk = set()
    backtrack(0, 0)

print(result)