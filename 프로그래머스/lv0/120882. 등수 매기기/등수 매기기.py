def solution(score):
    answer = [0] * len(score)
    avg = [((x[0] + x[1]) / 2) for x in score]
    cnt = 0

    for index, element in enumerate(avg):
        cnt = 1
        for num in avg:
            if (element != num) and (element < num):
                cnt += 1
        answer[index] = cnt        
    
    return answer