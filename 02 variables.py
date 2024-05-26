
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

#this is a main function 
def main():
    demo_variabe()


#call the main function 
main()