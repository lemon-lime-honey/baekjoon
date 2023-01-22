n = int(input())

for k in range(n):
    word, i, j = map(str, input().split())
    i = int(i)
    j = int(j)
    
    for index, letter in enumerate(word):
        if index not in range(i, j):
            print(letter, end ='')
    
    print()