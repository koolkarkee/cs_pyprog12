def is_matrix_multipliable(a: list, b: list):
    if len(a)*len(b) == 0:
        return (False, "matrix should not be empty.")
    else:
        col_no_first: int = len(a[0])
        row_no_second: int = len(b)
        if col_no_first != row_no_second:
            return (False, "number of columns in the first matrix doesn't match with number of rows in the second matrix")
        else:
            return(True, "matrix can be multiplied")
        
m1 : list = [[1, 2, 3], [4, 5, 6]]
m2 : list = [[3, 4, 5, 6], [2, 4, 6, 8]]

print(is_matrix_multipliable([], []))
print(is_matrix_multipliable(m1, m2))

#appending a row in m2, to make the matrix multipliable 
m2.append([1, 3, 5, 7])
print(is_matrix_multipliable(m1, m2))

print("matrix 1: ", m1)
print("matrix 2: ", m2)

#multiply the matrix
def multiply_matrices(x: list, y: list):
    multiplied = []
    # multiplied = [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0]
    # 
    print("col len of y", len(y[0]))

    for i in range(len(x)):  
        multiplied.append([])
        print(multiplied)

        for j in range(len(y[0])):  
            multiplied[i].append(0)

    print("multiplied matrix : ", multiplied)

    #rows 
    for i in range(len(x)):
        myrows = x[i]
        #print("my rows: ", myrows)

        #columns
        for j in range(len(y[0])):  
            #print("my cols: ", y[0])  
 
            for k in range(len(y)): 
                multiplied[i][j] += x[i][k] * y[k][j] 
            
    return multiplied

result = multiply_matrices(m1, m2)
print("multiplication of two matrices : ", result)

#second implementation
def multiply_matrices2(A : list, B: list):
    result = [] #output

    for i in range(len(A)):

        row = [] # the new row in new matrix
        for j in range(len(B[0])):
            
            product = 0 # the new element in the new row
            for v in range(len(A[i])):
                product += A[i][v] * B[v][j]
            row.append(product) # append sum of product into the new row
            
        result.append(row) # append the new row into the final result

    return result

#confirming previous output 
print("output 2 is ", multiply_matrices2(m1, m2))

#implementation via zip
def multiply_matrices3(X : list, Y: list):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

    return result

#confirming previous output 
print("output 3 is ", multiply_matrices3(m1, m2))
