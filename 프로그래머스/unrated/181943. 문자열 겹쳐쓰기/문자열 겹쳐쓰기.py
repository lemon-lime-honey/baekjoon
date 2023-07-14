def solution(my_string, overwrite_string, s):
    answer = list(my_string)
    for i in range(s, s + len(overwrite_string)):
        answer[i] = overwrite_string[i - s]
    return ''.join(answer)