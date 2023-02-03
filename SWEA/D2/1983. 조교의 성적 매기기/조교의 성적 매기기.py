grade_dict = {0: 'D0', 1: 'C-', 2: 'C0', 3: 'C+', 4: 'B-', 
              5: 'B0', 6: 'B+', 7: 'A-', 8: 'A0', 9: 'A+'}

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    score = list()
    grade = [None] * n
    
    for j in range(n):
        assignment = list(map(int, input().split()))
        temp = 0.35 * assignment[0] + 0.45 * assignment[1] + 0.2 * assignment[2]
        score.append((temp, j))
    
    score.sort()
    cycle = n // 10
    
    for j in range(n):
            grade[score[j][1]] = grade_dict[j // cycle]
    
    print(f'#{i + 1} {grade[k - 1]}')