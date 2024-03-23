string = input()
ppap = 'PPAP'

if string == ppap:
    print(ppap)
else:
    stack = list()
    ref = ['P', 'P', 'A', 'P']
    for letter in string:
        stack.append(letter)
        if stack[-4:] == ref:
            for i in range(4):
                stack.pop()
            stack.append('P')

    if ''.join(stack) == ppap or stack == ['P']:
        print(ppap)
    else:
        print('NP')