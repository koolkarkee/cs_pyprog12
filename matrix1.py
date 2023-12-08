m1 = [
    [1, 2, 3, 4], 
    [4, 5, 6, 7], 
    [8, 9, 0, 3] 
]

print("matrix : ", m1)

#transposed matrix 
transposed: list = []

#print number of columns and rows
print("number of columns: ", len(m1[0]))
print("number of rows: ", len(m1))

col_no: int = len(m1[0])
row_no: int = len(m1)

#n*m becomes m*n after transpose
for i in range(0, col_no):
    transposed.append(list())
    
for i in range(0, row_no):
    for j in range(0, col_no):
        print(m1[i][j])
        transposed[j].append(m1[i][j])
    print('next row') 

print("transposed matrix: ", transposed)

transposed2 : list = []
transposed2 = list(zip(*m1))
print("transposed 2: ", transposed2) 


