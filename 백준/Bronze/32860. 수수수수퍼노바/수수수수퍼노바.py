n, m = map(int, input().split())
target = list()

letters = [""]

for i in range(26):
    letters.append(chr(i + ord('a')))

first = m // 26
second = m % 26
target = None

if m <= 26:
    target = letters[m].upper()
elif second == 0:
    target = letters[first - 1] + letters[-1]
else:
    target = letters[first] + letters[second]

print(f"SN {n}{target}")