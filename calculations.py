#function for addition
def addition():
    row = get_row_number()
    column = get_column_number()

    matrix1 = []
    matrix2 = []
    result = []

    print("\n Enter the elements for the 1st Matrix :")
    matrix1 = matrix_take(row, column)
    print("\n 1st matrix is ")
    matrix_print(matrix1)

    print("\n Enter the elements for the 2nd matrix :")
    matrix2 = matrix_take(row,column)
    print("\n 2nd matrix is :")
    matrix_print(matrix2)
    for i in range(row):
        rows = []
        for j in range(column):
            value = matrix1[i][j] + matrix2[i][j]
            rows.append(value)
        result.append(rows)

    return result


#function to sub two matrix 
def subtraction():

    row = get_row_number()
    column = get_column_number()

    matrix1 = []
    matrix2 = []
    result = []
    print("\n Enter the elements for the 1st Matrix :")
    matrix1 = matrix_take(row, column)
    print("\n 1st matrix is ")
    matrix_print(matrix1)

    print("\n Enter the elements for the 2nd matrix :")
    matrix2 = matrix_take(row,column)
    print("\n 2nd matrix is :")
    matrix_print(matrix2)
    for i in range(row):
        rows = []
        for j in range(column):
            value = matrix1[i][j] - matrix2[i][j]
            rows.append(value)
        result.append(rows)
    return result


#function to multiplication two matrix
def multiplication():
    print("\n enter the row and column number for the 1st matrix :")
    row_for_1 = get_row_number()
    column_for_1 = get_column_number()

    print("\n enter the row and column number for the 2nd matrix :")
    row_for_2 = get_row_number()
    column_for_2 = get_column_number()

    if (column_for_1 == row_for_2):
        matrix1 = []
        matrix2 = []
        result = []
        print("\n Enter the elements for the 1st Matrix :")
        matrix1 = matrix_take(row_for_1, column_for_1)
        print("\n 1st matrix is ")
        matrix_print(matrix1)

        print("\n Enter the elements for the 2nd matrix :")
        matrix2 = matrix_take(row_for_2,column_for_2)
        print("\n 2nd matrix is :")
        matrix_print(matrix2)
        for i in range(row_for_1):
            rows = []
            for j in range(column_for_2):
                value = 0
                for k in range(column_for_1):
                    value = round(value + matrix1[i][k]*matrix2[k][j], 1)
                rows.append(value)
            result.append(rows)
        return result
    else:
        print("\n Enter the order of the matrixes correctly and try again")
        pass



#finction to calculate the determinante by taking a matrix from the code
def find_Determinante(matrix):
        if(len(matrix) == len(matrix[0])):
            determinant = 0
            # Base case for 1x1 matrix
            if len(matrix) == 1:
                return matrix[0][0]

            # Base case for 2x2 matrix
            if len(matrix) == 2:
                determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                return round(determinant, 3)

            # Iterate over the first row of the matrix
            for j in range(len(matrix)):
                cofactor = (-1) ** j * matrix[0][j]
                submatrix = [[matrix[i][k] for k in range(len(matrix)) if k != j] for i in range(1, len(matrix))]
                sub_determinant = find_Determinante(submatrix)
                determinant += cofactor * sub_determinant

            return round(determinant, 3)
        else :
            return matrix

#function to calculate the determinante for the very first matrix
def determinante_1st():
            order = get_order()
            matrix = []
            print("\n Enter the elements for the matrix:")
            matrix = matrix_take(order, order)
            print("\n the matrix is ")
            matrix_print(matrix)
         # Base case for 1x1 matrix
            if len(matrix) == 1:
                return matrix[0][0]

            # Base case for 2x2 matrix
            if len(matrix) == 2:
                determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
                return determinant
            determinant = 0
            # Iterate over the first row of the matrix
            for j in range(len(matrix)):
                cofactor = (-1) ** j * matrix[0][j]
                submatrix = [[matrix[i][k] for k in range(len(matrix)) if k != j] for i in range(1, len(matrix))]#kd
                sub_determinant = find_Determinante(submatrix)
                determinant += cofactor * sub_determinant
            return round(determinant, 3)


#function to calculate the transpose of a matrix
def transpose():
    row = get_row_number()
    column = get_column_number()

    transposed = []
    print("\n Enter the matrix :")

    matrix = matrix_take(row, column)

    print("\n The matrix is :")
    matrix_print(matrix)

     
    for i in range(column):
        transposed.append([0] * row)
    
    for i in range(row):
        for j in range(column):
            transposed[j][i] = matrix[i][j]
    return transposed


#function to find the cofactor for adjoint
def get_cofactor_adjoint(matrix, i, j):
    # Remove the i-th row and j-th column from the matrix
    return [[matrix[row][col] for col in range(len(matrix[row])) if col != j] for row in range(len(matrix)) if row != i]

#function to find the adjoint of a matrix very fast
def adjoint():
    print("\n Enter the order of the matrix")
    order = get_order()

    print("\n Enter the elements for the matrix")
    matrix = matrix_take(order, order)
    print("\n matrix is :")
    matrix_print(matrix)
    adjoint = []
    for i in range(order):
            adjoint_row = []
            for j in range(order):
                # Calculate the cofactor matrix
                cofactor = get_cofactor_adjoint(matrix, i, j)
                # Calculate the determinant of the cofactor matrix
                cofactor_determinant = find_Determinante(cofactor)
                # Multiply by (-1)^(i+j)
                sign = (-1) ** (i + j)
                value = round(sign * cofactor_determinant, 1)
                adjoint_row.append(value)
            adjoint.append(adjoint_row)
        # Transpose the adjoint matrix
    adjoint = transpose_pre(adjoint)
    return adjoint


#function to calculate inverse of the matrix very fast
def inverse():
    print("\n enter the order of the matrix :")
    order = get_order()
    print("\n enter the elements for the matrix :")
    matrix = matrix_take(order, order)
    print("\n The matrix is :")
    matrix_print(matrix)
    total_determinante = find_Determinante(matrix)
    adjoint = []
    for i in range(order):
                adjoint_row = []
                for j in range(order):
                    # Calculate the cofactor matrix
                    cofactor = get_cofactor_adjoint(matrix, i, j)
                    # Calculate the determinant of the cofactor matrix
                    cofactor_determinant = find_Determinante(cofactor)
                    # Multiply by (-1)^(i+j)
                    sign = (-1) ** (i + j)
                    value = round((sign * cofactor_determinant) / total_determinante , 1)
                    adjoint_row.append(value)
                adjoint.append(adjoint_row)
            # Transpose the adjoint matrix
    adjoint = transpose_pre(adjoint)
    return adjoint
