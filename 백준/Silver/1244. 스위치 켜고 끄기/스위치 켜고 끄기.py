switch = int(input())
state = [0] + list(map(int, input().split()))
students = int(input())

for i in range(students):
    student, number = map(int, input().split())
    if student == 1:
        for j in range(number, switch + 1, number):
            if state[j] == 0:
                state[j] = 1
            else:
                state[j] = 0
    elif student == 2:
        for j in range(switch // 2):
            if number + j > switch or number - j < 1: break
            if state[number + j] == state[number - j]:
                if state[number + j] == 0:
                    state[number + j] = 1
                    state[number - j] = 1
                else:
                    state[number + j] = 0
                    state[number - j] = 0
            else: break

for i in range(1, switch + 1):
    print(state[i], end=' ')
    if not i % 20: print()