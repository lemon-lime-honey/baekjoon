substring = set()
s = input()

for i in range(len(s)):
    for j in range(len(s)):
        if i <= j:
            substring.add(s[i:j + 1])

print(len(substring))