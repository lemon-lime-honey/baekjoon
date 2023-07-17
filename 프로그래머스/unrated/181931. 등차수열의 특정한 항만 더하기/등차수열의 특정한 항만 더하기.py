def solution(a, d, included):
    n = len(included)
    answer = 0

    for i in range(n):
        if included[i]: answer += a + d * i

    return answer