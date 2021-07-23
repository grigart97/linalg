import math
from les_2.matrix_dot_det import matrix_det, MyError, rows1_columns2_check


def simmetic_check(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                raise MyError('Матрица несиметрична. Данный метод не применим. Используйте другой')


def det_check(matrix):
    if matrix_det(matrix) == 0:
        raise MyError('Матрица вырождена. Данный метод не применим. Используйте другой')


def holeckiy(matrix: [list], b: []) -> []:
    rows1_columns2_check(matrix, matrix)
    rows1_columns2_check(matrix, b)
    det_check(matrix)
    simmetic_check(matrix)
    L = []
    for i, el_i in enumerate(matrix):
        L.append([])
        for j, el_j in enumerate(el_i):
            if j == i:
                L[i].append(math.sqrt(el_j - sum([L[i][k] ** 2 for k in range(i)])))
            elif j < i:
                L[i].append((el_j - sum([L[i][k] * L[j][k] for k in range(j)])) / L[j][j])
    y = []
    for i, el_i in enumerate(b):
        y.append((el_i - sum([L[i][j] * y[j] for j in range(i)])) / L[i][i])
    x = []
    size = len(b)
    for i, el_i in enumerate(reversed(y)):
        x.append((el_i - sum([L[size - j - 1][size - i - 1] * x[j] for j in range(i)])) / L[size - i - 1][size - i - 1])
    print(x)
    return L


a = [[81, -45, 45],
     [-45,  50, -15],
     [45, -15, 38]]
b = [531, -460, 193]
holeckiy(a, b)
