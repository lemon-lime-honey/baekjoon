letters = "abcdefghijklmnopqrstuvwxyz"
s = input()

idx = 0
result = 0

while idx < len(s):
    result += 1
    for letter in letters:
        if s[idx] == letter:
            idx += 1
        if idx >= len(s):
            break

print(result)
