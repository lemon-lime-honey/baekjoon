def solution(answers):
    pattern_one = [1, 2, 3, 4, 5]
    pattern_two = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [[0, 1], [0, 2], [0, 3]]

    answer = list()
    
    for index, value in enumerate(answers):
        if pattern_one[index % 5] == value:
            score[0][0] += 1
        if pattern_two[index % 8] == value:
            score[1][0] += 1
        if pattern_three[index % 10] == value:
            score[2][0] += 1
    
    score.sort(reverse = True)
    answer.append(score[0][1])
    if score[0][0] == score[1][0]:
        answer.append(score[1][1])
    if score[0][0] == score[2][0]:
        answer.append(score[2][1])
    
    return answer[::-1]