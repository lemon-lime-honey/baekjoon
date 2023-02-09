alphabet = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())

for i in range(t):
    ipt = input()
    result = 0

    for index, letter in enumerate(ipt):
        if letter == alphabet[index]:
            result += 1
        else:
            break
    
    print(f'#{i + 1} {result}')