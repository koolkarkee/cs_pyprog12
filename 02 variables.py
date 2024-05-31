
#user defined function 
def demo_variabe():
    #dynamically typed variable (you don't need to specify the type)
    x = 2   
    print(x)

    #prints the memory address of x
    print(id(x))

    #print the type of x
    print(type(x))

    pi = 3.14
    #f-string 
    print(f"\ntype of pi = {type(pi)} and value of pi = {pi}")  

def demo_del():
    price : float = 20.4
    print(price)
    print(id(price))

    #another variable with same value
    price_2 = 20.4
    print(id(price_2)) #output: references memory of price

    price_3 = 20.5
    print(id(price_3))

    del(price)
    #print(price)

    print(price_2)

#this is a main function 
def main():
    #demo_variabe()
    demo_del()


#call the main function 
main()