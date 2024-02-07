#!/usr/bin/python3
""" A module that computes Pascal's triangle"""


def pascal_triangle(n):
    """ Returrns pascal's triangle"""
    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                previous_row = triangle[row - 1]
                current_row.append(previous_row[col - 1] + previous_row[col])
        triangle.append(current_row)
    return triangle
