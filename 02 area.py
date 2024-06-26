PI = 3.14

#user defined function
def area_of_circle(radius):
    area = PI * radius * radius
    print(f"The area of circle is : {area}")

#x5 + x3 + 3x2 + 2x + 1
def cubic_function(x):
    #value = x*x*x*x*x + x*x*x + 3*x*x + 2*x + 1
    value = x**5 + x**3 + 3* (x**2) + 2*x + 1
    print(f"The value of cubic function is {value}")

def sin(x):
    #sinx = x - x3/3! + x5/5! - x7/7!
    value1 = (x ** 3)/6 
    value2 = (x ** 5)/120
    value3 = (x ** 7)/5040

    final_value = x - value1 + value2 - value3
    print(final_value)


#main function 
def main():
    area_of_circle(7)
    cubic_function(0)
    cubic_function(7)
    sin(30)

main()