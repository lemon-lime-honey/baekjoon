letter = ['0,', '0', '0', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
word = list(input())

for i in word:
    for j in letter:
        if i in j:
            time += letter.index(j)

print(time)