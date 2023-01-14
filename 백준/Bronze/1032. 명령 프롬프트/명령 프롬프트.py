n = int(input())
words = list()
result = list()

for i in range(n):
    words.append(input())

for i in range(len(words[0])):
    letter = words[0][i]

    for word in words:
        if word[i] != letter:
            result.append('?')
            break
    else:
        result.append(words[0][i])

print(''.join(result))