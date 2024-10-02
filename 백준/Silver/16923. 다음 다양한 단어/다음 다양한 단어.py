ipt = input()
alphabet = [False for i in range(26)]

if len(ipt) != 26:
    for letter in ipt:
        alphabet[ord(letter) - ord('a')] = True

    for idx, tf in enumerate(alphabet):
        if not tf:
            print(ipt, chr(ord('a') + idx), sep='')
            break
else:
    target = -1
    for i in range(25, 0, -1):
        alphabet[ord(ipt[i]) - ord('a')] = True
        for j in range(ord(ipt[i]) - ord('a') + 1, 26):
            if alphabet[j]:
                target = j
                break
        if target != -1:
            print(ipt[:i], chr(target + ord('a')), sep='')
            break
    else:
        print(-1)
