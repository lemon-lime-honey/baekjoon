from collections import defaultdict

n = int(input())
letter_dict = defaultdict(set)

for i in range(n):
    letters = [0 for i in range(26)]
    word = input()
    for letter in word:
        letters[ord(letter) - ord("a")] += 1
    letter_dict[tuple(letters)].add(word)

print(len(letter_dict.values()))
