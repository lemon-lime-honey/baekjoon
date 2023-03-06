def solution(s):
    number = list(map(int, s.split(' ')))
    answer = str(min(number)) + ' ' + str(max(number))
    return answer