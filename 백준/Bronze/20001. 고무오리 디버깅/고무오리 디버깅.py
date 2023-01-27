problem = list()

while True:
    command = input()
    if command == '고무오리 디버깅 끝':
        if not problem:
            print('고무오리야 사랑해')
            break
        else:
            print('힝구')
            break
    elif command == '고무오리':
        if problem:
            problem.pop()
        else:
            problem.append(True)
            problem.append(True)
    elif command == '문제':
        problem.append(True)