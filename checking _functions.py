#function for the menu
def menu():
    print(" Your options are :")
    print(" for addtion > +\n for subtraction > -\n for multiplication > *\n for determinante > d\n for transpose > t\n for adjoint > a\n for inverse > i")
    return correct_menu_choice()

#function to take correct menu choice
def correct_menu_choice():
    while True:
        choice = input("\n what you want :").lower()
        ex_choice_correct = r'[\+\-\*dtai]'
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
        except ValueError:
            pass

#function to take correct row number
def get_row_number():
    while True:
        try :
            return int(input("\n Enter the row number :"))
        except ValueError:
            pass

#function to take correct column number 
def get_column_number():
    while True:
        try:
            return int(input("\n Enter the column number :"))
        except ValueError:
            pass

#function to take correct element
def get_element(i,j):
     while True:
        try:
            return complex(input(f"\n Enter the element for {i+1},{j+1} :"))
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
