def solution(numbers, hand):
    pad = {1: (1, 1), 2: (1, 2), 3: (1, 3),
           4: (2, 1), 5: (2, 2), 6: (2, 3),
           7: (3, 1), 8: (3, 2), 9: (3, 3),
           0: (4, 2), -1: (4, 1), -2: (4, 3)}
    answer = list()
    left = -1
    right = -2

    for number in numbers:
        if number in (1, 4, 7):
            left = number
            answer.append('L')
        elif number in (3, 6, 9):
            right = number
            answer.append('R')
        else:
            ldist = abs(pad[number][0] - pad[left][0]) \
                    + abs(pad[number][1] - pad[left][1])
            rdist = abs(pad[number][0] - pad[right][0]) \
                    + abs(pad[number][1] - pad[right][1])

            if ldist < rdist:
                left = number
                answer.append('L')
            elif ldist > rdist:
                right = number
                answer.append('R')
            elif hand == 'left':
                left = number
                answer.append('L')
            else:
                right = number
                answer.append('R')

    return ''.join(answer)