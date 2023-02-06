def solution(box, n):
    size = list()
    
    for i in range(3):
        size.append(box[i] // n)

    answer = size[0] * size[1] * size[2]

    return answer