j, n = map(int, input().split())
result = 0

for i in range(n):
    ipt = input()
    score = 0
    
    for letter in ipt:
        if letter.isdigit():
            score += 2
        elif letter.isspace():
            score += 1
        elif letter.islower():
            score += 2
        else:
            score += 4

    if score <= j:
        result += 1

print(result)