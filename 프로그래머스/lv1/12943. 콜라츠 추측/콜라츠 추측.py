def solution(num):
    if num == 1:
        return 0

    answer = 0

    while True:
        answer += 1
        if not (num % 2):
            num //= 2
        else:
            num = num * 3 + 1
        if num == 1:
            break
        if answer == 500:
            return -1

    return answer