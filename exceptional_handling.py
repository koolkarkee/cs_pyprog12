num = input("enter numerator : ")
den = input("enter denominator : ")

#checking exception
try:
    div = num/den
    print(f"division is :  {div}")
except:
    print("exception occured 1..")

#check again after type casting to int
try:
    if (int(den)) == 0:
        raise ZeroDivisionError("The denominator is zero and therefore the division cannot be found.")
    
    div = (int(num))/(int(den))
    #div = num/den

    #print(f"division is :  {div}")
except ZeroDivisionError as zde:
    print("exception occured 2 ..")
    print("Exception details 2 : ", zde.args)
except Exception as ex:
    print("Exception details 3 : ", ex.args)
else:
    print(f"Value : {div}")
finally:
    print("I'm going to close the connection ... ")

