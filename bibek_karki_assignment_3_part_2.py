#10 Write a program to check whether a year entered is leap or not.
def is_leap_year(year: int):
    if(year % 4 == 0 and year%100 != 0 or year%400 == 0):
        return 'is a leap year'
    else:
        return 'is not a leap year'
    
print(f"Year 2024 {is_leap_year(2024)}")
print(f"Year 2036 {is_leap_year(2036)}") 
print("--------------------------------")

#11 Write a program to display “MDS” 10 times.
for i in range(10):
    print("MDS")
print("--------------------------------")

#12 Write a program to find sum and average of 10 numbers stored in a list.
list_ten_numbers = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]
sum_list_ten_numbers = 0

for i in range(0, len(list_ten_numbers)):
    sum_list_ten_numbers += list_ten_numbers[i]

print(f"The sum of the ten numbers in the list is : {sum_list_ten_numbers}")
print(f"The average of the ten numbers in the list is : {sum_list_ten_numbers/len(list_ten_numbers)}")

print("--------------------------------")

#13 Write a program to display prime numbers up to 100.
def is_prime_number(n: int):
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n%i == 0:
                is_prime = False
    return is_prime

def list_prime_numbers(total: int):
    list_prime_numbers = list()

    for n in range(1, total):
        if(is_prime_number(n)):
            list_prime_numbers.append(n)

    return list_prime_numbers

print(f"The list of prime numbers from 1 to 100 is : {list_prime_numbers(100)}")
print("--------------------------------")

#14 Write a program to find sum of digits of a number.
def calc_sum_of_digits(number: int):
    sum_of_digits = 0
    my_str_number = str(number)

    for i in range(0, len(my_str_number)):
        try:
            sum_of_digits += int(my_str_number[i])
        except ValueError as ve:
            sum_of_digits += 0 

    return sum_of_digits

print(f"The sum of digits of the number 12345.6 is {calc_sum_of_digits('12345.6')}")
print("--------------------------------")

#15 Write a program to check whether a number is palindrome or not.
def check_palindrome(number: int):
    temp = number
    reverse = 0

    while number > 0:
        digit = number%10
        reverse = reverse*10 + digit
        number = number//10
    
    return 'is a palindrome' if temp == reverse else 'is not a palindrome' 

print(f"The number 121 {check_palindrome(121)}")
print(f"The number 1212 {check_palindrome(1212)}")
print("--------------------------------")

#16 Write a program to check if a number is Armstrong Number or not.
def check_armstrong_number(number: int):
    sum = 0

    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    return 'is an armstrong number' if number == sum else 'is not an armstrong number'

print(f"The number 123 {check_armstrong_number(123)}")
print(f"The number 370 {check_armstrong_number(370)}")
print("--------------------------------")

#17 Write a program to count number of vowels in a string.
def count_vowels(word: str):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    lower = word.lower()

    for i in range(0, len(lower)):
        for j in range(0, len(vowels)):
            if lower[i] == vowels[j]:
                count += 1 
                print(lower[i])
    
    return count

print(f"The number of vowels in the word Elephant is {count_vowels('Elephant')}")
print(f"The number of vowels in the word apple is {count_vowels('apple')}")
print("--------------------------------")

#18 Write a program to find smallest and largest number among 10 numbers stored in a list.
def find_smallest_largest_number(a: list):
    smallest = 0
    largest = 0

    for i in range(0, len(a)):
        if smallest > a[i]:
            smallest = a[i]
        if largest < a[i]:
            largest = a[i]

    return (smallest, largest)

my_test_list = [2, 4, 6, 8, 10, 12, 14, -1, -30, 100]
print(f"The smallest and largest number in the list is respectively : {find_smallest_largest_number(my_test_list)}")
print("--------------------------------")

#19 Write a program to count even numbers and odd numbers stored in a list.
def count_even_odd_numbers(a: list):
    count_even = 0
    count_odd = 0

    for i in range(0, len(a)):
        if a[i]%2 == 0:
            count_even += 1
        else:
            count_odd += 1
    
    return (count_even, count_odd)

print(f"The number of even and odd numbers in the list is respectively : {count_even_odd_numbers(my_test_list)}")
print("--------------------------------")

#20 Write a program to find sum of two matrices.
X = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]
Y = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]

def sum_two_matrices(a: list, b: list):
    result = [
        [0, 0, 0],
        [0, 0, 0], 
        [0, 0, 0]
    ]

    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    
    return result

print(f"The sum of two matrices is : {sum_two_matrices(X, Y)}") 
print("--------------------------------")

#21 Write a program to find product of two matrices.
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
print("--------------------------------")

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
print("--------------------------------")

#22 Write a program using list comprehension to find sum of only even numbers.
my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

count = [x for x in my_list if x%2 == 0] 
print(f"The sum of the even numbers in the list is : {count}") 
print("--------------------------------")

#23 Write a program using function with return type to find sum of two numbers.
def sum_of_two_numbers(a: int, b: int) -> int:
    return a+b

print(f"The sum of 2 and 3 is {sum_of_two_numbers(2, 3)}")
print(
    "--------------------------------")
#24 Write a program using recursive function to find factorial of a number.
def recur_factorial(n: int):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
   
def show_factorial(num: int):
    if num < 0:
        print("No factorial for negative number!")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print(f"The factorial of {num} is {recur_factorial(num)}")

show_factorial(-1)
show_factorial(0)
show_factorial(5)
print("--------------------------------")

#25 Write a program using recursive function to find nth Fibonacci number.
def fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
 
print(f"The 6th fibonacci number is : {fibonacci(6)}")
print(f"The 10th fibonacci number is : {fibonacci(10)}")
print("--------------------------------")


