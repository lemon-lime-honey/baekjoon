def solution(n, numlist):
    answer = list()
    
    for number in numlist:
        if not (number % n):
            answer.append(number)

    return answer