import re

#function for the menu
def menu():
    print(" for addtion > +\n for subtraction > -\n for multiplication > *\n for determinante > d\n for transpose > t\n for adjoint > a\n for inverse > i")
    return correct_menu_choice()

#function to take correct menu choice
def correct_menu_choice():
    while True:
        choice = input("\n what you want :").lower()
        ex_choice_correct = r'[\+\-\*\dd\dt\da\di]'
        if re.match(ex_choice_correct, choice):
            return choice
        else:
            pass

#function to valid reuse choice
def reuse_choice():
    while True:
        choice = input("\n Is you want to use your last ans as one of the next input (y/n):").lower()
        if re.match(r'^[yn]$', choice):
            return choice
        else:
            pass

#function to reuse the matrix as in multiplication as 1st or 2nd
def multiplication_choice_matrix():
    while True:
        choice = input("\n fir which matrix you want to use as 1st or 2nd (1/2)")
        if re.match(r'^[12]$', choice):
            return choice
        else:
            pass

#function to take the order of the matrix for determinante
def get_order():
    while True:
        try :
            return int(input("\n Enter the order number :"))
            break
        except ValueError:
            pass

#function to take correct row number
def get_row_number():
    while True:
        try :
            return int(input("\n Enter the row number :"))
            break
        except ValueError:
            pass

#function to take correct column number 
def get_column_number():
    while True:
        try:
            return int(input("\n Enter the column number :"))
            break
        except ValueError:
            pass

#function to take correct element
def get_element(i,j):
     while True:
        try:
            return int(input(f"\n Enter the element for {i+1},{j+1} :"))
            break
        except ValueError:
            pass

#function to take the matrix
def matrix_take(row, column):
    matrix  = []
    for i in range(row):
        rows=[]
        for j in range(column):
            value = get_element(i,j)
            rows.append(value)
        print()
        matrix.append(rows)
    return matrix

#function to print the matrix
def matrix_print(matrix):
    for rows in matrix:
        print(f"{rows}")
    print()

#function to add two matrix
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

#function to add two matrix using result
def addition_pre(matrix1):
    print("\n 1st matrix is ")
    matrix_print(matrix1)
    print("\n Enter the row and column for the 2nd matrix :")
    row = get_row_number()
    column = get_column_number()
    row_1 = len(matrix1)
    column_1 = len(matrix1[0])
    if (row_1 == row and column_1 == column):
        matrix2 = []
        result = []

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
    else :
        return matrix1

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

#function to sub two matrix using result
def subtraction_pre(matrix1):
    print("\n 1st matrix is ")
    matrix_print(matrix1)
    print("\n Enter the number of row and column for the 2nd matrix :")
    row = get_row_number()
    column = get_column_number()
    row_1 = len(matrix1)
    column_1 = len(matrix1[0])
    if(row_1 == row and column_1 == column):
        matrix2 = []
        result = []

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
    else:
        return matrix1

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

#function to multiply two matrix using result
def multiplication_pre(matrix):
    matrix_choice = multiplication_choice_matrix()
    if(matrix_choice == "1"):
        print("\n 1st matrix is ")
        matrix_print(matrix)
        print("\n Enter the row and column number for the 2nd matrix :")
        row_for_2 = get_row_number()
        column_for_2 = get_column_number()
        matrix2 = []
        result = []
        row_for_1 = len(matrix)
        column_for_1 = len(matrix[0])

        if (column_for_1 == row_for_2):

            print("\n Enter the elements for the 2nd matrix :")
            matrix2 = matrix_take(row_for_2,column_for_2)
            print("\n 2nd matrix is :")
            matrix_print(matrix2)
            
            for i in range(row_for_1):
                rows = []
                for j in range(column_for_2):
                    value = 0
                    for k in range(column_for_1):
                        value = round(value + matrix[i][k]*matrix2[k][j], 1)
                    rows.append(value)
                result.append(rows)
            return result
        else:
            
            return matrix
    else:
        print("\n 2nd matrix is ")
        matrix_print(matrix)
        print("\n Enter the row and column number for the 1st matrix :")
        row_for_1 = get_row_number()
        column_for_1 = get_column_number()
        matrix1 = []
        result = []
        row_for_2 = len(matrix)
        column_for_2 = len(matrix[0])

        if (column_for_1 == row_for_2):

            print("\n Enter the elements for the 2nd matrix :")
            matrix1 = matrix_take(row_for_1,column_for_1)
            print("\n 2nd matrix is :")
            matrix_print(matrix1)
            
            for i in range(row_for_1):
                rows = []
                for j in range(column_for_2):
                    value = 0
                    for k in range(column_for_1):
                        value = round(value + matrix1[i][k]*matrix[k][j], 1)
                    rows.append(value)
                result.append(rows)
            return result
        else:
            
            return matrix

#finction to calculate the determinante middle of the code
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

#function to calculate the transpose of a matrix middle in the code
def transpose_pre(matrix):
    row = len(matrix)
    column = len(matrix[0])
    transposed = []
    
    for i in range(column):
        rows = []
        for j in range(row):
            value = 0
            rows.append(value)
        transposed.append(rows)
    
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

#function to find adjoint of a marix middile in the code
def adjoint_pre(matrix):
    row = len(matrix)
    column = len(matrix[0])
    if(row == column):
        order = len(matrix)
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
    else :
        return matrix

#function to find the inverse of a matrix middle of the code
def inverse_pre(matrix):
    row = len(matrix)
    column = len(matrix[0])
    total_determinante = find_Determinante(matrix)
    if total_determinante != 0:
        if(row == column):
            order = len(matrix)
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
                    value = round((sign * cofactor_determinant) / total_determinante, 1)
                    adjoint_row.append(value)
                adjoint.append(adjoint_row)
            # Transpose the adjoint matrix
            adjoint = transpose_pre(adjoint)
            return adjoint
        else :
            print("\n matrix is not square matrix.")
            return matrix
    else:
        print(f"\n determinnante of the matrix is {total_determinante} so it is not invertable. ")
        return matrix

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

#main function
def main():
    res_matrix = []
    all_answer = []
    
    no_of_ans = 0
    no =0
    des = "n"
    const = "n"
    hello = 0
    if(hello == 0):
        print("WELCOME TO ph03n1x CALCULATOR \n")
        hello += 1
    
    while True:
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if (no != 0):
            print("\n Previous result is :")
            matrix_print(res_matrix)
            des = reuse_choice()
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if (des != "y"):
            choice = menu()
            if (choice == "+"):
                res_matrix = addition()
                print("\n result is :")
                matrix_print(res_matrix)
                no += 1
                no_of_ans += 1
                all_answer.append(res_matrix)
            elif(choice == "a"):
                res_matrix = adjoint()
                print("\n adjoint of the matrix is :")
                matrix_print(res_matrix)
                no += 1
                no_of_ans += 1
                all_answer.append(res_matrix)
            elif(choice == "t"):
                res_matrix = transpose()
                print("\n transpose is :")
                matrix_print(res_matrix)
                no +=1 
                no_of_ans += 1
                all_answer.append(res_matrix)
            elif (choice == "-"):
                res_matrix = subtraction()
                print("\n result is :")
                matrix_print(res_matrix)
                no +=1
                no_of_ans += 1
                all_answer.append(res_matrix)
            elif (choice == "d"):
                determin = determinante_1st()
                print(f"\n determinante is {determin}")
                no = 0
                des = "n"
                #no_of_ans += 1
                #all_answer.append(res_matrix)
            elif (choice == "i"):
                res_matrix = inverse()
                print("\n Inverse is :")
                matrix_print(res_matrix)
                no += 1
                no_of_ans += 1
                all_answer.append(res_matrix)
            else:
                res_matrix = multiplication()
                print("\n result is :")
                matrix_print(res_matrix)
                no += 1
                no_of_ans += 1
                all_answer.append(res_matrix)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        else:#kd
            choice = menu()
            if (choice == "+"):
                res_matrix1 = addition_pre(res_matrix)
                if (res_matrix != res_matrix1):
                    res_matrix = res_matrix1
                    print("\n result is :")
                    matrix_print(res_matrix)
                    no += 1
                    no_of_ans += 1
                    all_answer.append(res_matrix)
                else:
                    print("\n you enter a wrong order matrix to do further calculation.")
                    no += 1
            elif(choice == "a"):
                res_matrix1 = adjoint_pre(res_matrix)
                if(res_matrix != res_matrix1):
                    res_matrix = res_matrix1
                    print("\n adjoint of the matrix is :")
                    matrix_print(res_matrix)
                    no += 1
                    no_of_ans += 1
                    all_answer.append(res_matrix)
                else:
                    print("\n the order of the matrix is not same.")
                    no += 1
            elif(choice == "t"):
                res_matrix1 = transpose_pre(res_matrix)
                if(res_matrix != res_matrix1):
                    res_matrix = res_matrix1
                    print("\n transpose is :")
                    matrix_print(res_matrix)
                    no += 1
                    no_of_ans += 1
                    all_answer.append(res_matrix)
                else:
                    print("\n Invalid input or transpose is same")
                    no += 1
            elif(choice == "i"):
                res_matrix1 = inverse_pre(res_matrix)
                if(res_matrix != res_matrix1):
                    res_matrix = res_matrix1
                    print("\n Inverse is :")
                    matrix_print(res_matrix)
                    no += 1
                    no_of_ans += 1
                    all_answer.append(res_matrix)
                else:
                    pass #seem function to see the reply
            elif(choice == "-"):
                res_matrix1 = subtraction_pre(res_matrix)
                if (res_matrix != res_matrix1):
                    res_matrix = res_matrix1
                    print("\n result is :")
                    matrix_print(res_matrix)
                    no += 1
                    no_of_ans += 1
                    all_answer.append(res_matrix)
                else:
                    print("\n You enter a wrong order matrix to do further calculation.")
                    no += 1
            elif (choice == "d"):
                determinante = find_Determinante(res_matrix)
                if (determinante != res_matrix):
                    print(f"\n determinante is {determinante}")
                    no = 0
                    des = "n"
                    #no_of_ans += 1
                    #all_answer.append(determinante)
                else:
                    print("\n we can't find the determinante of the matrix")
                    matrix_print(res_matrix)
                    no += 1
            else:
                res_matrix1 = multiplication_pre(res_matrix)
                if (res_matrix != res_matrix1):
                    res_matrix = res_matrix1
                    print("\n result is :")
                    matrix_print(res_matrix)
                    no += 1
                    no_of_ans += 1
                    all_answer.append(res_matrix)
                else:
                    print("\n You enter a wrong order matrix to do further calculation.")
                    no += 1
        
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
        ask = input("\n Press any key to continue or press n to exit . ")
        
        if ask.lower() == const:
            print(" your reseltis are :")
            for i in range(0 , no_of_ans):
                matrix_print(all_answer[i])
            break
        else:
            continue

main()