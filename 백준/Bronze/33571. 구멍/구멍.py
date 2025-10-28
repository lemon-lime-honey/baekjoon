s = input()
result = 0

for letter in s:
    if letter in "AabDdegOoPpQqR@":
        result += 1
    elif letter == "B":
        result += 2

print(result)
