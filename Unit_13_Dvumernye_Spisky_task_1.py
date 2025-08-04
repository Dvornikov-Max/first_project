import random

def generate_matrix(rows, cols, low=-50, high=50):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(low, high))
        matrix.append(row)
    return matrix


def sum_matrices(m1, m2):
    if len(m1) != len(m2) or any(len(row1) != len(row2) for row1, row2 in zip(m1, m2)):
        raise ValueError("Матрицы должны быть одинакового размера для сложения")

    rows = len(m1)
    cols = len(m1[0])
    result = []
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(m1[i][j] + m2[i][j])
        result.append(result_row)
    return result


def print_matrix(matrix, name="Матрица"):
    print(f"{name} ({len(matrix)}x{len(matrix[0])}):")
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    #Для матриц 10x10
    rows, cols = 10, 10
    matrix_1 = generate_matrix(rows, cols)
    matrix_2 = generate_matrix(rows, cols)
    matrix_3 = sum_matrices(matrix_1, matrix_2)

    print_matrix(matrix_1, "Матрица 1")
    print_matrix(matrix_2, "Матрица 2")
    print_matrix(matrix_3, "Сумма двух матриц")

    #Для матриц 4x3
    rows2, cols2 = 4, 3
    m1_4x3 = generate_matrix(rows2, cols2)
    m2_4x3 = generate_matrix(rows2, cols2)
    sum_4x3 = sum_matrices(m1_4x3, m2_4x3)

    print_matrix(m1_4x3, "Мини-матрица - 1")
    print_matrix(m2_4x3, "Мини-матрица - 2")
    print_matrix(sum_4x3, "Сумма мини-сатриц 4x3")