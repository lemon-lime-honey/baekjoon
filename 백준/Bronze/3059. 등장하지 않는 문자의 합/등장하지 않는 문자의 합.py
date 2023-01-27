alpha = [chr(x) for x in range(65, 91)]

t = int(input())

for i in range(t):
    string = input()
    total = 0
    chk = [False] * 26
    
    for letter in string:
        for j in range(26):
            if alpha[j] == letter:
                chk[j] = True
                break
    
    for j in range(26):
        if not chk[j]:
            total += ord(alpha[j])
    
    print(total)