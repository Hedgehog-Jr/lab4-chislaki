def gauss(a_matrix, b_vector, n):
    x_vector = [None] * n
    for k in range(n):
        for i in range(k + 1, n):
            if abs(a_matrix[i][k]) > abs(a_matrix[k][k]):
                a_matrix[i], a_matrix[k] = a_matrix[k], a_matrix[i]
                b_vector[i], b_vector[k] = b_vector[k], b_vector[i]
        a_main = a_matrix[k][k]
        if a_main == 0:
             print("Решение системы невозможно")
             exit("Определитель матрицы равен нулю")
        for i in range(k, n):
            a_matrix[k][i] /= a_main
        b_vector[k] /= a_main
        for i in range(k + 1, n):
            subtracted = a_matrix[i][k]
            for j in range(k, n):
                a_matrix[i][j] -= subtracted * a_matrix[k][j]
            b_vector[i] -= subtracted * b_vector[k]
    for k in range(n - 1, -1, -1):
        x_vector[k] = b_vector[k]
        for i in range(n - 1, k, -1):
            x_vector[k] -= a_matrix[k][i] * x_vector[i]
    return x_vector
