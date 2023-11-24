def solution(arr):
    def solve(r, c, n):
        if n == 1:
            answer[arr[r][c]] += 1
            return

        flag = False

        for i in range(r, n + r):
            if flag: break
            for j in range(c, n + c):
                if arr[i][j] != arr[r][c]:
                    flag = True
                    break

        if flag:
            one = solve(r, c, n // 2)
            two = solve(r, c + n // 2, n // 2)
            three = solve(r + n // 2, c, n // 2)
            four = solve(r + n // 2, c + n // 2, n // 2)
        else:
            answer[arr[r][c]] += 1


    answer = [0, 0]
    solve(0, 0, len(arr))

    return answer