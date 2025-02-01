n = int(input())

target = input()
result = 0

for i in range(n - 1):
    word = input()
    letters = list(target)
    cnt = 0

    for letter in word:
        if letter in letters:
            letters.remove(letter)
        else:
            cnt += 1

    if cnt < 2 and len(letters) < 2:
        result += 1

print(result)
