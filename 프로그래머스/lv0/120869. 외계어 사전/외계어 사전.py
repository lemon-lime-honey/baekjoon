def solution(spell, dic):
    answer = 0
    spellset = set(spell)
    flag = False

    for word in dic:
        wordset = set()
        for letter in word:
            if (letter in spellset) and (letter not in wordset):
                wordset.add(letter)
            else:
                break
        else:
            if len(spellset) == len(wordset):
                flag = True
    
    if flag:
        answer = 1
    else:
        answer = 2

    return answer