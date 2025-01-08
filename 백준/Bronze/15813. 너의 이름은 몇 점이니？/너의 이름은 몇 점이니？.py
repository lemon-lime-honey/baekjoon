n = int(input())
name = input()

score = 0

for letter in name:
    score += ord(letter) - ord("A") + 1

print(score)
