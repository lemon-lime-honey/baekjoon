def solution(array, commands):
    answer = list()
    
    for element in commands:
        i, j, k = element
        temp = array[i - 1: j]
        temp.sort()
        answer.append(temp[k - 1])
    
    return answer