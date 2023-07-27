def solution(n):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = [[0 for i in range(n)] for j in range(n)]
    pos = [0, 0]
    ref = 0
    for i in range(1, n ** 2 + 1):
        answer[pos[0]][pos[1]] = i
        nr = pos[0] + direction[ref][0]
        nc = pos[1] + direction[ref][1]
        if nr < 0 or nc < 0 or nr >= n or nc >= n or answer[nr][nc] != 0:
            ref = (ref + 1) % 4
            nr = pos[0] + direction[ref][0]
            nc = pos[1] + direction[ref][1]
        pos = [nr, nc]
    return answer