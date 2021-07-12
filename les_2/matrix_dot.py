class MyError(Exception):
    def __init__(self, text):
        self.txt = text


def matrix_dot(matrix1: [list], matrix2: [list]) -> [list]:
    if len(matrix1) != len([el for el in matrix1 if len(el) == len(matrix1[0])]) and \
            len(matrix2) != len([el for el in matrix2 if len(el) == len(matrix2[0])]):
        raise MyError('Количество элементов в строках матриц должны совпадать')
    if len(matrix2) != len(matrix1[0]):
        raise MyError('Количество столбцов первой матрицы должно совподать с количеством строк во второй матрице')
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
