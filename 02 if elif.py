
x:int = int(input("Enter a number"))
y:int = int(input("Enter a number"))

#divide
z = x/y

if  z < 0:
    print("z is less than 0")
elif z > 0:
    print("z is greater than 0")
elif z == 0:
    print("z is equal to zero")
else:
    print("Unknown")