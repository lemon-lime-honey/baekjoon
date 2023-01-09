n = int(input())
cnt = 0
for i in range(n):
    temp = input()
    last = ''
    alpha = dict()
    for letter in temp:
        if letter not in alpha:
            alpha[letter] = 1
            last = letter
        else:
            if letter != last:
                break
            else:
                alpha[letter] += 1
    else:
        cnt += 1
print(cnt)