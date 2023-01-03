import sys

while True:
    case = sys.stdin.readline().strip().split()
    if case[0] == '#':
        break
    else:
        if (int(case[1]) > 17) or (int(case[2]) >= 80):
            print(f'{case[0]} Senior')
        else:
            print(f'{case[0]} Junior')