def solution(num, k):
    number = list(str(num))
    answer = 0
    
    for i in range(len(number)):
        if number[i] == str(k):
            answer = i + 1
            break
    else:
        answer = -1

    return answer