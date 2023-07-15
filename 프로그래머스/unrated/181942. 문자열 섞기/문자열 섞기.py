def solution(str1, str2):
    length = len(str1)
    answer = list()

    for i in range(length):
        answer.append(str1[i])
        answer.append(str2[i])

    return ''.join(answer)