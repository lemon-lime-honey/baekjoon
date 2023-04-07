def mul_matrix(m1, m2):
    res = [[0 for i in range(2)] for j in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += m1[i][k] * m2[k][j] % 1000000007
    return res


def exp(a, b):
    if b == 1: return a
    res = exp(a, b // 2)
    return mul_matrix(mul_matrix(res, res), a) if b % 2 else mul_matrix(res, res)


n = int(input())
matrix = [[1, 1], [1, 0]]
final_matrix = exp(matrix, n)

print(final_matrix[0][1] % 1000000007)