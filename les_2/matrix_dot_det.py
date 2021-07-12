class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def rows_len_check(matrix):
    if len(matrix) != len([el for el in matrix if len(el) == len(matrix[0])]):
        raise MyError('Количество элементов в строках матрицы должны совпадать')


def rows1_columns2_check(matrix1, matrix2):
    if len(matrix2) != len(matrix1[0]):
        raise MyError('Количество столбцов первой матрицы должно совподать с количеством строк во второй матрице')


def matrix_det(matrix):
    rows_len_check(matrix)
    rows1_columns2_check(matrix, matrix)
    det = 0
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    for i, num in enumerate(matrix[0]):
        det += (-1) ** i * num * matrix_det(
            [[el for j, el in enumerate(vector) if j != i] for k, vector in enumerate(matrix) if k > 0]
        )
    return det


def matrix_dot(matrix1: [list], matrix2: [list]) -> [list]:
    rows_len_check(matrix1)
    rows_len_check(matrix2)
    rows1_columns2_check(matrix1, matrix2)
    answer = []
    for i in range(len(a)):
        answer.append([])
        for j in range(len(b[0])):
            answer[i].append(0)
            for w in range(len(b)):
                answer[i][j] += matrix1[i][w] * matrix2[w][j]
    return answer


if __name__ == '__main__':
    a = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    b = [[1, 2, 3], [4, 5, 6]]
    print(matrix_dot(a, b))

    c = [[1, 2, 3, 4],
         [9, -2, 10, 6],
         [4, 0, 17, -4],
         [3, 1, 1, 111]]
    print(matrix_det(c))
