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
