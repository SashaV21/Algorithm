"""
n, m, k = map(int, input().split())
matr =[]

for _ in range(n):
    s = list(map(int, input().split()))
    matr.append(s)

for _ in range(k):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            ans += matr[i][j]
    print(ans)
"""
import numpy as np


def build_2d_prefix_sum_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        return np.array([])  # Возвращаем пустой NumPy массив для пустой матрицы

    prefix_sum_matrix = np.zeros((rows + 1, cols + 1), dtype=int)

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_sum_matrix[i, j] = (
                    matrix[i - 1][j - 1]
                    + prefix_sum_matrix[i - 1, j]
                    + prefix_sum_matrix[i, j - 1]
                    - prefix_sum_matrix[i - 1, j - 1]
            )

    return prefix_sum_matrix[1:, 1:]  # Возвращаем матрицу без первого ряда и столбца из нулей


n, m, k = map(int, input().split())
matr = []
for _ in range(n):
    s = list(map(int, input().split()))
    matr.append(s)
matr = build_2d_prefix_sum_matrix(matr)
print(matr)
