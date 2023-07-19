def solution(my_strings, parts):
    answer = list()
    n = len(parts)
    for i in range(n):
        answer.append(my_strings[i][parts[i][0]:parts[i][1] + 1])
    return ''.join(answer)