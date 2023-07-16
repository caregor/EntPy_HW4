"""
    ---Task 1---
Напишите функцию для транспонирования матрицы.
"""


def transpose_matrix(matrix):
    if not matrix:
        return []

    if len(matrix[0]) == 0:
        return []

    transposed = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


transposed = transpose_matrix(matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)
print("Транспонированная матрица:")
for row in transposed:
    print(row)