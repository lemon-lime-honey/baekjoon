from sys import exit

ipt = input()
duck = list()
result = 0

letterDict = {'q': 'k', 'u': 'q', 'a': 'u', 'c': 'a', 'k': 'c'}

for letter in ipt:
    if letter == 'q' and not duck: duck.append([letter])
    else:
        for sound in duck:
            if sound[-1] == letterDict[letter]:
                sound.append(letter)
                break
        else:
            if letter == 'q': duck.append([letter])
            else:
                print(-1)
                exit()

for sound in duck:
    if not len(sound) % 5: result += 1
    else:
        print(-1)
        exit()

print(result if result else -1)