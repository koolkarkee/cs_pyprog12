x : int = 5
PI : float = 3.1415

print(x)

def square_of_the_number(x):
    return x ** 2

def power(base, power):
    return base ** power

def volume_of_cylinder(radius, height):
    return PI * (radius**2) * height

def main():
    #x = float(input("Enter a number"))
    #print(f"Square of x is = {square_of_the_number(x)}")
    #print(f"{square_of_the_number("Bibek Karki ")}")
    #y = power("Bibek Karki ", 3)
    p = power(3.1415, 2)
    print(p)
    
    r = float(input("Enter the radius"))
    h = float(input("Enter the height"))
    v = volume_of_cylinder(r,h)
    print(f"Volume is {v}") 

main()