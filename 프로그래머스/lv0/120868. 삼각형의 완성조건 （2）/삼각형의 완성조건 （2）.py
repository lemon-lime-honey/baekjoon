def solution(sides):
    sides.sort()
    answer = 0
    side = 1
    
    while side < sum(sides):
        if (side < sides[1]) and (side + sides[0] > sides[1]):
            answer += 1
        elif (sides[1] <= side) and (side < sum(sides)):
            answer += 1
        side += 1
    
    return answer