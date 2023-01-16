vowel = 'aeiou'

n = int(input())
s = input()
cnt = 0

for letter in s:
    if letter in vowel:
        cnt += 1

print(cnt)