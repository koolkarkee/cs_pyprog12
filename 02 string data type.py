
#str class in python 
str = "Rita Budhathoki"
print(f"Type of str is {type(str)}")

#length of string : len(str)
print(f"Length of string = {len(str)}")

#index of string : str[index]
print(f"5th index is = {str[5]}") 

#concat string : using + operator 
print("Rita " + "Budhathoki")
print(str + " Thapa Kaji")

#concat string : using * operator (repetition)
print("Apple*3")
print("Apple" * 5)

#for i in range(0,10,1):print("0" * i)

#slicing string : [2:5]
print(str[2:5]) #includes 2 and excludes 5
print(str[4:12])

#strings are immutable 
name = "Sita Karki"
print(name[0]) 

#name[0] = 'G'
#print(name)