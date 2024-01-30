#!/usr/bin/python3
""" a script that divides a list by a number """

def matrix_divided(matrix, div):
    new_matrix = [[]]
    result = all(len(row) == len(matrix[0]) for row in matrix)
    if not result:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if (not isinstance(matrix, list) or matrix == [] or
    not all(isinstance(row, list) for row in matrix or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row]))):
                raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        new_row = []
        for elem in i:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix
