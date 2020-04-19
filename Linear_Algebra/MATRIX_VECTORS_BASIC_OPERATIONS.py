import numpy as np

matrix1 = np.array([[2, -7, 5], [-6, 2, 0]])
matrix2 = np.array([[5, 8, -5], [3, 6, 9]])
num = 2

# matrix addition:
def matrix_add(matrix1, matrix2):
    add_operation = np.add(matrix1, matrix2)
    return add_operation

# matrix subtraction:
def matrix_subt(matrix1, matrix2):
    subt_operation = np.subtract(matrix1, matrix2)
    return subt_operation

# scalar-matrix multiplication:
def sc_mat_mult(matrix1, num):
    sc_mat_operation = np.dot(num, matrix1)
    return sc_mat_operation

# scalar-matrix division:
def sc_mat_div(matrix1, num):
    sc_matrix_op = np.divide(matrix1, num)
    return sc_matrix_op

# matrix-matrix multiplication:
def mat_mat_mult(matrix1, matrix2):
    m_m_mult = np.multiply(matrix1, matrix2)
    return m_m_mult





