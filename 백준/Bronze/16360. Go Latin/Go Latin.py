table = {
    "a": "as",
    "i": "ios",
    "y": "ios",
    "l": "les",
    "n": "anes",
    "ne": "anes",
    "o": "os",
    "r": "res",
    "t": "tas",
    "u": "us",
    "v": "ves",
    "w": "was"
}

n = int(input())

for i in range(n):
    word = input()
    for eng in table.keys():
        if word[len(word) - len(eng):] == eng:
            print(word[:len(word) - len(eng)], table[eng], sep="")
            break
    else:
        print(word, "us", sep="")
