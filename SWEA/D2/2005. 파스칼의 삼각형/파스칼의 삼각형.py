t = int(input())

for i in range(t):
    n = int(input())
    print(f'#{i + 1}')
    
    for i in range(n):
        pascal = list()
        temp = 11 ** i
        
        while temp > 0:
            pascal.append(temp % 10)
            temp //= 10
        
        print(*pascal)