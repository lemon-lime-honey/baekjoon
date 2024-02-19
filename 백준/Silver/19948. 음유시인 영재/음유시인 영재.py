poem = input().split()
space = int(input())
keyboard = list(map(int, input().split()))
title = list()

if len(poem) - 1 > space:
    print(-1)
else:
    for word in poem:
        title.append(word[0].upper())
        idx = 0
        while idx < len(word):
            keyboard[ord(word[idx].lower()) - ord('a')] -= 1
            if idx < len(word) - 1 and word[idx] == word[idx + 1]:
                while idx < len(word) - 1 and word[idx] == word[idx + 1]:
                    idx += 1
                idx += 1
            else:
                idx += 1

    idx = 0
    while idx < len(title):
        keyboard[ord(title[idx]) - ord('A')] -= 1
        if idx < len(title) - 1 and title[idx] == title[idx + 1]:
            while idx < len(title) - 1 and title[idx] == title[idx + 1]:
                idx += 1
            idx += 1
        else:
            idx += 1

    for n in keyboard:
        if n < 0:
            print(-1)
            break
    else:
        print(''.join(title))