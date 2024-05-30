#either true or false/Yes or No/1 or 0
#True or False
am_I_hungry : bool = True 
am_I_thirsty : bool = False

print(am_I_hungry)
print(am_I_thirsty)

print(not am_I_hungry)
print(not am_I_thirsty)

print(not not am_I_hungry)

value =  (input("Are you sure you want to exit? Y/N?"))
if value is "Y":
    print(True)
elif value is "N":
    print(False)
else:
    print("Error")
