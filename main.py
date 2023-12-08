def is_greater(value:int):
    return value > 100

a = 5
#print(is_greater(a := 7000))


##reverse a list
fruits = list() 
fruits = ['apple', 'oranges', 'mangoes', 'bananas', 23, 55]

reverse_list = list()

'''
for i in range(len(fruits) -1, -1, -1):  
    #print(fruits[i])
    reverse.append(fruits[i])
    
print(reverse)
'''

import copy as cp
reverse_list = cp.deepcopy(fruits)
reverse_list.reverse()

#print(fruits)
#print(reverse_list) 

a = [1, 2, 3]
b = [4, 5, 6]

d = a + b
#print(d)

c = list()
for i in range(0, len(a)):
    #elem = (a[i], b[i])
    #c.append(elem)
    a[i] = a[i]**3

print(a)

#problem 9: Remove all occurances of a Specific Item if Found
list_numbers = [1, 1, 3, 3, 3, 3, 5, 5, 5, 5, 6, 8, 8, 8, 9, 9, 9]
print("original list (of numbers): ", list_numbers)

def remove_all_occurances_if_item_found(list_occurances:list, list_occurances_item: int):    
    if list_occurances_item not in list_occurances:  
        return list_occurances
    else:
        list_occurances.remove(list_occurances_item) 
        return remove_all_occurances_if_item_found(list_occurances, list_occurances_item)

print("current list (of numbers after removing 1): ", remove_all_occurances_if_item_found(list_numbers, 1))
print("current list (of numbers after removing 3): ", remove_all_occurances_if_item_found(list_numbers, 3))
print("current list (of numbers after removing 5): ", remove_all_occurances_if_item_found(list_numbers, 5))

        
    


