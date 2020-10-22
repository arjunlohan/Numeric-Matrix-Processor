import math
def menu():
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose Matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")


def transpose_menu():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")


def matrix_enter_1(x):
    global error_matrix_1
    for i in range(0, int(x)):
        entry = input()
        entry = entry.split(" ")
        matrix_1.append(entry)
    for i in range(0, int(x)):
        if len(matrix_1[i]) == int(x):
            pass
        else:
            error_matrix_1 += 1


def matrix_enter_2(x):
    global error_matrix_2
    for i in range(0, int(x)):
        entry = input()
        entry = entry.split(" ")
        matrix_2.append(entry)
    for i in range(0, int(x)):
        if len(matrix_2[i]) == int(x):
            pass
        else:
            error_matrix_2 += 1


def matrix_sum(one, two):
    for row in range(int(one)):
        col = []
        for column in range(int(two)):
            if matrix_1[row][column].isdigit() and matrix_2[row][column].isdigit():
                col.append(str(int(matrix_1[row][column]) + int(matrix_2[row][column])))
            else:
                col.append(str(float(matrix_1[row][column]) + float(matrix_2[row][column])))
        sum_matrix.append(col)
        print(*col, sep=" ")


def matrix_multiply_constant(one, two, three):
    for row in range(int(one)):
        col = []
        for column in range(int(two)):
            if three.isdigit():
                if matrix_1[row][column].isdigit():
                    col.append(str(int(matrix_1[row][column]) * int(three)))
                else:
                    col.append(str(float(matrix_1[row][column]) * float(three)))
            else:
                col.append(str(float(matrix_1[row][column]) * float(three)))
        multiply_matrix.append(col)
        print(*col, sep=" ")


def matrix_multiply(one, two):
    X = one
    global matrix_3
    Y = two
    col = []
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            total = 0
            for k in range(len(Y)):
                if X[i][k].isdigit() and Y[k][j].isdigit():
                    total += int(X[i][k]) * int(Y[k][j])
                else:
                    total += float(X[i][k]) * float(Y[k][j])
            total = round(total, 2)
            col.append(str(total))

                #col.append(str(float(matrix_1[row][column]) * float(matrix_2[row][column])))
    matrix_3 =[col[i:i+int(len(col)/len(X))] for i in range(0, len(col), int(len(col)/len(X)))]
    for col in matrix_3:
        print(*col, sep=" ")


def matrix_transpose_main(mat):
    global transpose_matrix
    transpose_matrix = mat
    transpose_matrix = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return transpose_matrix


def matrix_transpose_side(mat):
    global transpose_matrix
    transpose_matrix = mat
    for row in range(int(len(mat[0]))):
        mat[row] = mat[row][::-1]
    transpose_matrix = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    for row in range(int(len(transpose_matrix[0]))):
        transpose_matrix[row] = transpose_matrix[row][::-1]
    return transpose_matrix


def matrix_transpose_vertical(mat):
    global transpose_matrix
    transpose_matrix = mat
    for row in range(int(len(mat[0]))):
        mat[row] = mat[row][::-1]
    transpose_matrix = mat
    return transpose_matrix


def matrix_transpose_horizontal(mat):
    global transpose_matrix
    transpose_matrix = mat
    mat = mat[::-1]
    transpose_matrix = mat
    return transpose_matrix


def matrix_determinant(A, total=0):
    if len(A) == 1:
        return int(A[0][0])
    else:
        if str(A[0][0]).isdigit():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] = int(A[i][j])
        else:
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] = float(A[i][j])

        indices = list(range(len(A)))
        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val
        for fc in indices:
            As = A.copy()
            As = As[1:]
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc + 1:]
            sign = (-1) ** (fc % 2)  # F)
            sub_det = matrix_determinant(As)
            total += sign * A[0][fc] * sub_det
        return total


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def matrix_inverse(m, total=0):
    determinant = round(matrix_determinant(m),3)
    if determinant == 0:
        print("This matrix doesn't have an inverse.")
    else:
        # special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]

        # find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = getMatrixMinor(m, r, c)
                cofactorRow.append(round(((-1) ** (r + c)) * matrix_determinant(minor),3))
            cofactors.append(cofactorRow)
        cofactors = matrix_transpose_main(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = round(cofactors[r][c] / determinant,3)
        return cofactors



while_loop_condition = True
while while_loop_condition:
    matrix_1 = []
    matrix_2 = []
    sum_matrix = []
    multiply_matrix = []
    matrix_3 = []
    transpose_matrix = []
    error_matrix_1 = 0
    error_matrix_2 = 0
    menu()
    choice = input("Your choice: ")
    if choice == "1":
        size_matrix_1 = input("Enter size of first matrix: ")
        size_matrix_1_row = size_matrix_1.replace(" ", "")
        print("Enter first matrix:")
        matrix_enter_1(size_matrix_1_row[0])
        size_matrix_2 = input("Enter size of second matrix: ")
        size_matrix_2_row = size_matrix_2.replace(" ", "")
        matrix_enter_2(size_matrix_2_row[0])
        if int(size_matrix_1_row[0]) == int(size_matrix_2_row[0]) and int(size_matrix_2_row[1]) == int(size_matrix_1_row[1]):
            print("The result is:")
            matrix_sum(size_matrix_1_row[0], size_matrix_2_row[1])
        else:
            print("ERROR")
    elif choice == "2":
        size_matrix_1 = input("Enter size of first matrix: ")
        size_matrix_1_row = size_matrix_1.replace(" ", "")
        print("Enter first matrix:")
        matrix_enter_1(size_matrix_1_row[0])
        constant = input("Enter constant: ")
        if int(size_matrix_1_row[0]) == int(len(matrix_1)) and int(size_matrix_1_row[1]) == int(len(matrix_1[0])):
            print("The result is:")
            matrix_multiply_constant(size_matrix_1_row[0], size_matrix_1_row[1], constant)
        else:
            print("ERROR")
    elif choice == "3":
        size_matrix_1 = input("Enter size of first matrix: ")
        size_matrix_1_row = size_matrix_1.replace(" ", "")
        print("Enter first matrix:")
        matrix_enter_1(size_matrix_1_row[0])
        size_matrix_2 = input("Enter size of second matrix: ")
        size_matrix_2_row = size_matrix_2.replace(" ", "")
        matrix_enter_2(size_matrix_2_row[0])
        print("The result is:")
        if int(size_matrix_1_row[1]) == int(size_matrix_2_row[0]):
            matrix_multiply(matrix_1, matrix_2)
        else:
            print("ERROR")
    elif choice == "4":
        transpose_menu()
        transpose_choice = input("Your choice: ")
        size_matrix_1 = input("Enter matrix size: ")
        size_matrix_1_row = size_matrix_1.replace(" ", "")
        print("Enter matrix:")
        matrix_enter_1(size_matrix_1_row[0])
        print("The result is:")
        if transpose_choice == "1":
            for row in matrix_transpose_main(matrix_1):
                print(*row, sep=" ")
        elif transpose_choice == "2":
            for row in matrix_transpose_side(matrix_1):
                print(*row, sep=" ")
        elif transpose_choice == "3":
            for row in matrix_transpose_vertical(matrix_1):
                print(*row, sep=" ")
        elif transpose_choice == "4":
            for row in matrix_transpose_horizontal(matrix_1):
                print(*row, sep=" ")
        else:
            print("ERROR")
    elif choice == "5":
        size_matrix_1 = input("Enter matrix size: ")
        size_matrix_1_row = size_matrix_1.replace(" ", "")
        print("Enter matrix:")
        matrix_enter_1(size_matrix_1_row[0])
        matrix_determinant(matrix_1)
        print("The result is:")
        print(matrix_determinant(matrix_1))
    elif choice == "6":
        size_matrix_1 = input("Enter matrix size: ")
        size_matrix_1_row = size_matrix_1.replace(" ", "")
        print("Enter matrix:")
        matrix_enter_1(size_matrix_1_row[0])
        print("The result is:")
        data = matrix_inverse(matrix_1)
        rows = [line for line in data]
        cols = zip(*rows)
        col_widths = [max(len(str(value)) for value in col) for col in cols]
        format_2 = ' '.join(['%%%ds' % width for width in col_widths])
        for row in rows:
            print(format_2 % tuple(row))

    elif choice == "0":
        while_loop_condition = False
        pass
    else:
        print("ERROR")