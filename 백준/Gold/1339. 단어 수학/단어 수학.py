n = int(input())
letters = dict()
ten = [i for i in range(10)]
words = [input() for i in range(n)]
result = 0

for word in words:
    for i in range(len(word)):
        if word[i] not in letters:
            letters[word[i]] = 10 ** (len(word) - 1 - i)
        else:
            letters[word[i]] += 10 ** (len(word) - 1 - i)

numbers = sorted(list(letters.values()), reverse=True)

for number in numbers:
    result += number * ten.pop()

print(result)