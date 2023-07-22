def solution(num_list):
    answer = 0
    for number in num_list:
        chk = number
        while chk > 1:
            if chk % 2:
                chk = (chk - 1) // 2
            else:
                chk //= 2
            answer += 1
    return answer