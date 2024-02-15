word = input()
flag = True

if (word[-1] != 'f' or
    word[0] != 'w' or
    len(word) < 4):
    flag = False

wolf = {'w': 0, 'o': 1, 'l': 2, 'f': 3}
cnt = [1, 0, 0, 0]

for i in range(1, len(word)):
    if not flag: break

    chk = wolf[word[i]] - wolf[word[i - 1]]

    if chk == -3:
        for num in cnt:
            if num != cnt[0]:
                flag = False
                break
        else:
            cnt[wolf[word[i]]] += 1
    elif chk in (0, 1):
        cnt[wolf[word[i]]] += 1
    else:
        flag = False
        break

if flag:
    for num in cnt:
        if num != cnt[0]:
            flag = False
            break

print(1 if flag else 0)