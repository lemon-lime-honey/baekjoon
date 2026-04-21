s = int(input())

for i in range(s):
    vowel, consonant = 0, 0
    target = input()

    for letter in target:
        if letter.isalpha():
            if letter in "AEIOUaeiou":
                vowel += 1
            else:
                consonant += 1

    print(consonant, vowel)
