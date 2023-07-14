from itertools import permutations

def solution(babbling):
    can = ['aya', 'ye', 'woo', 'ma']
    words = set()
    answer = 0

    for i in range(1, 5):
        temp = permutations(can, i)
        for word in temp:
            words.add(''.join(word))

    for word in babbling:
        if word in words: answer += 1

    return answer