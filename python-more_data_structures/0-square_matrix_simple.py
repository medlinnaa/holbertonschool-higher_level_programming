#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix=[]
    for x in matrix:
        for y in x:
            sq_matrix.append(y**2)
            return sq_matrix
