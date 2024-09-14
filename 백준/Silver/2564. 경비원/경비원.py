import sys
input = sys.stdin.readline


def get_dist(direction, distance):
    match direction:
        case 1:
            return distance
        case 2:
            return a + b + (a - distance)
        case 3:
            return a + b + a + (b - distance)
        case 4:
            return a + distance


a, b = map(int, input().split())
n = int(input())
position = list()
result = 0

for i in range(n + 1):
    position.append(tuple(map(int, input().split())))

person_dist = get_dist(*position[-1])

for i in range(n):
    chk = get_dist(*position[i])
    result += min(
        abs(person_dist - chk),
        2 * (a + b) - abs(person_dist - chk)
    )

print(result)
