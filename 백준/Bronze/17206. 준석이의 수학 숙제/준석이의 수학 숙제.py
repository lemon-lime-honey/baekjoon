def three(n):
   if n < 3:
       return 0
   else:
       return (3 + (n // 3) * 3) * (n // 3) // 2

def seven(n):
    if n < 7:
        return 0
    else:
        return (7 + (n // 7) * 7) * (n // 7) // 2

def twentyOne(n):
    if n < 21:
        return 0
    else:
        return (21 + (n // 21) * 21) * (n // 21) // 2

t = int(input())
n = list(map(int, input().split()))
for number in n:
    print(three(number) + seven(number) - twentyOne(number))