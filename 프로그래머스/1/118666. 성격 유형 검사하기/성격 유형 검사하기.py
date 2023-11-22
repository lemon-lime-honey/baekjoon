def solution(survey, choices):
    score = {1: 3, 2: 2, 3: 1, 5: 1, 6: 2, 7: 3}
    types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    typeCnt = [0 for i in range(8)]

    for i in range(len(survey)):
        if choices[i] < 4:
            typeCnt[types.index(survey[i][0])] += score[choices[i]]
        elif choices[i] > 4:
            typeCnt[types.index(survey[i][1])] += score[choices[i]]

    answer = list()

    for i in range(0, 8, 2):
        if typeCnt[i] < typeCnt[i + 1]:
            answer.append(types[i + 1])
        else:
            answer.append(types[i])

    return ''.join(answer)