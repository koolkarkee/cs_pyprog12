#1 Write a program display “Hello World!”.
print("Hello World!")
print("--------------------------------")


#2 Write a program to find sum of two numbers. Use input() function to take input from the user.

#basic implementation
def add(a: int, b: int):
    return a+b 

print(f"3 + 5 is {add(3,5)}")
print(f"3 + 5. is {add(3,5.)}")

#another implementation using input() function
first_num = int(input("Input the first number : "))
sec_num = int(input("Input the second number : "))

print(f"The sum of two numbers {first_num} and {sec_num} is {add(first_num, sec_num)}")
print("--------------------------------")


#3 Write a program to calculate discount on the basis of following assumption:
#If purchased amount is greater than or equal to 1000, discount is 5%

purchased_amount = int(input("Enter the purchased amount : "))
def calc_discount(): 
    return 0 if purchased_amount < 1000 else (0.05 * purchased_amount)

print(f"The discount amount is: {calc_discount()}")  

#4 Write a program to calculate discount on the basis of following assumption:
# a) If purchased amount is greater than or equal to 1000, discount is 5%
# b) If purchased amount is less than 1000, discount is 3% 
def calc_discount2():
    return (0.03 * purchased_amount) if purchased_amount < 1000 else (0.05 * purchased_amount)

print(f"The second discount amount is: {calc_discount2()}")  
print("--------------------------------")

#5 Write a program to calculate discount on the basis of following assumption:
#a) If purchased amount is greater than or equal to 5000, discount is 10%
#b) If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
#c) If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
#d) If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
#e) If purchased amount is less than 2000, discount is 2%

def calc_discount3():
    discount_percentage = 0

    if purchased_amount >= 5000:
        discount_percentage = 10
    elif purchased_amount >= 4000 and purchased_amount < 5000:
        discount_percentage = 7
    elif purchased_amount >= 3000 and purchased_amount < 4000:
        discount_percentage = 5
    elif purchased_amount >= 2000 and purchased_amount < 3000:
        discount_percentage = 3
    elif purchased_amount < 2000:
        discount_percentage = 2

    return discount_percentage * purchased_amount * 0.01

print(f"The thrid discount amount is: {calc_discount3()}")  
print("--------------------------------")

#6 Write a program to calculate the simple interest on the basis of following assumption:
#a) If balance is greater than 99999, interest is 7 %
#b) If balance is greater than or equal to 50000 and less than 100000 interest is 5 %
#c) If balance is less than 50000, interest is 3%
balance = int(input("Enter the balance amount : "))

def calc_simple_interest(years: int):
    if balance > 99999:
        interest = 7
    elif balance >= 50000 and balance < 100000:
        interest = 5
    elif balance < 50000:
        interest = 3
    
    return (balance * years * interest)/100

print(f"The simple interest amount for 2 years is: {calc_simple_interest(2)}")  
print("--------------------------------")

#7 Write a program to test whether a number is even or odd.
def test_even_odd(number: int):
    return 'even' if number%2 == 0 else 'odd'

test_number = int(input("Enter a number to test even or odd: "))
print(f"{test_number} is {test_even_odd(test_number)} number") 
print("--------------------------------")

#8 Admission to a professional course is subject to the following conditions:
#a) Marks in mathematics >=60
#b) Marks in physics >=50
#c) Marks in chemistry >=40
#d) Total in all three subjects >=200
# Or
# Total in mathematics and physics>=150
# Given the marks in three subjects, write a program to process the applications to list eligible
# candidates. 

def admitted_professional_course(marks_maths: int, marks_physics: int, marks_chemistry: int):
    eligible = False

    if marks_maths >= 60 and marks_physics >= 50 and marks_chemistry >= 40 and (marks_maths + marks_chemistry + marks_maths) >= 200 or (marks_maths + marks_physics) >= 150:
        eligible = True  

    return "is eligible" if eligible else "not eligible"

print(f"The candidate is {admitted_professional_course(70, 40, 80)}")
print(f"The candidate is {admitted_professional_course(70, 50, 80)}")
print("--------------------------------")

#9 The rates of tax on gross salary are as shown below:
# Income Tax
# Less than 10,000 Nill
# Rs. 10,000 to 19,999 10%
# Rs. 20,000 to 39,999 15%
# Rs. 40,000 to above 20%
# Write a program to compute the net salary after deducting the tax for the given information
# and print the same.

gross_salary = int(input("Enter the gross salary : "))
def calc_net_salary():
    tax_rate = 0

    if gross_salary < 10000:
        tax_rate = 0
    elif gross_salary >= 10000 and gross_salary <= 19999:
        tax_rate = 10
    elif gross_salary >= 20000 and gross_salary <= 39999:
        tax_rate = 15
    elif gross_salary >= 40000:
        tax_rate = 20
    
    return (1 - (tax_rate/100)) * gross_salary

print(f"The net salary of gross salary is {calc_net_salary()}")
print("--------------------------------")
