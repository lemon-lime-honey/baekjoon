def solution(num_list):
    answer = 0
    if len(num_list) > 10:
        for number in num_list:
            answer += number
    else:
        answer = 1
        for number in num_list:
            answer *= number
    return answer