word = input()
cnt = 0

for letter in word:
    if letter in 'aeiou': cnt += 1

print(cnt)