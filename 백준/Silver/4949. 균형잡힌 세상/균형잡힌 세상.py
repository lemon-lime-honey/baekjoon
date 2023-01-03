import sys

def bracket(line):
    record = []
    flag = 0
    
    for letter in line:
        if letter == '(':
            record.append('(')
        elif letter == ')':
            if (len(record) != 0) and (record[-1] == '('):
                record.pop()
            else:
                flag = 1
                break
        elif letter == '[':
            record.append('[')
        elif letter == ']':
            if (len(record) != 0) and (record[-1] == '['):
                record.pop()
            else:
                flag = 1
                break
    if flag == 1:
        return 'no'
    if len(record) == 0:
        return 'yes'
    else:
        return 'no'

while True:
    line = sys.stdin.readline().rstrip()
    if line[0] == '.':
        break
    else:
        print(bracket(line))