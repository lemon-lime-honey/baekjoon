import sys

while True:
    sentence = sys.stdin.readline().strip().lower()
    if sentence == '#':
        break
    else:
        result = 0
        for letter in sentence:
            if letter in 'aeiou':
                result += 1
        print(result)