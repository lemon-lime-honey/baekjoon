words = input().split()
result = list()

for word in words:
    idx = 0
    while idx < len(word):
        result.append(word[idx])
        if word[idx] not in "aeiou":
            idx += 1
        else:
            idx += 3
    result.append(" ")

print("".join(result).strip())
