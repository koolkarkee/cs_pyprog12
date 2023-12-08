#problem 1: reverse a list

#implementation via append method
def reverse_list(val: list):
    return_val = list()
    for i in range(len(val) -1, -1, -1):
        return_val.append(val[i])
    return return_val

#test:
list_marks = [20, 40, 44, 94, 49]
print("marks before reversing : ", list_marks)
print("marks after reversing (first method) : ", reverse_list(list_marks))

#implementation via reverse method
import copy as cp
def reverse_list_via_reverse(val:list):
    return_val = cp.deepcopy(val)
    return_val.reverse()
    return return_val

#test 
print("marks after reversing (second method) : ", reverse_list_via_reverse(list_marks))

#problem 2: concatenate two lists (simple concatenation)
list_subjects = ["maths", "science", "english", "social", "nepali"]
print("concatenated list : ", list_marks + list_subjects)

#alternative implementation
list_grades = [1, 2, 3, 4, 5]
list_grades.extend(['A', 'B', 'C', 'D', 'E'])
print("concatenated list using extend method : ", list_grades)

#problem 2: concatenate two lists (by index concatenation)
def concatenate_list_by_index(a:list, b:list):
    concatenated_list = list()
    for i in range(0, len(a)):
        elem = (a[i], b[i])
        concatenated_list.append(elem)
    return concatenated_list

#test
print("concatenated list (by index) : ", concatenate_list_by_index(list_marks, list_subjects))

#problem 3: turn every item of a list into a square
def power_list_item(a:list, exp: int):
    new_list = cp.deepcopy(a)
    for i in range(0, len(a)):
        new_list[i] = new_list[i] ** exp

    return new_list

#test
print("list before squaring ", list_marks)
print("list after squaring ", power_list_item(list_marks, 2))
print("list after cubing ", power_list_item(list_marks, 3))

#problem 4: iterate two lists simultaneously
def iterate_lists_simultaneously(val1: list, val2:list):
    print("display power of zip : ")
    print("subject", "marks")
    for a, b in zip(val1, val2):
        print(b, a)

#test
iterate_lists_simultaneously(list_marks, list_subjects)

#problem 5: removal of empty strings from a list of elements 
def remove_empty_string(a: list):
    return_list = cp.deepcopy(a)
    while("" in return_list):
        return_list.remove("")
    
    return return_list

#implementation using filter method
def remove_empty_string_using_filter(a: list):
    return_list = cp.deepcopy(a)
    result = list(filter(None, return_list))
    
    return result

#test
list_empty_strings_to_operate = ["Hello ", "", "", "I'm", "Bibek.", ""]
print("Before removing empty strings : ", list_empty_strings_to_operate)
print("After removing empty strings (using while syntax) : ", remove_empty_string(list_empty_strings_to_operate))
print("After removing empty strings (using filter method) : ", remove_empty_string_using_filter(list_empty_strings_to_operate))

#problem 6: Add new Item to a List After a Specified Item
#using insert method
list_saarc = ["india", "nepal", "bangladesh", "bhutan"]
print("Before (using insert method) : ", list_saarc)

#to append at a desired index or an item
list_saarc.insert(len(list_saarc) - 1, "pakistan")
print("After (using insert method)", list_saarc)

#to append at the end
list_saarc.append("srilanka")
print("After using append method", list_saarc)
 
#problem 7: Extend a nested list by adding a Sublist
list_brics = ["brazil", "russia", "vietnam", "china", "south africa", list_saarc]  
print(list_brics)
sublist = ["uk", "usa"]
list_brics[5].extend(sublist)
print("Adding a country to saarc within brics :",  list_brics)

#problem 8: Replace the list Item with new Value if Found
def replace_list_item(a:list, val: str, replacement: str):
    temp = cp.deepcopy(a)
    for i in range(0, len(a)):
        if temp[i] == val:
            temp[i] = replacement
        elif temp[i] == "usa":
            temp[i] = "us"
    
    return temp

#test
print("before replacing india : ", list_saarc)
print("after replacing india : ", replace_list_item(list_saarc, "india", "congo"))

#problem 9: Remove all occurances of a Specific Item if Found
list_numbers = [1, 1, 3, 3, 3, 3, 5, 5, 5, 5, 6, 8, 8, 8, 9, 9, 9]
print("original list (of numbers): ", list_numbers)

def remove_all_occurances_if_item_found(list_occurances:list, list_occurances_item: int): 
    temp_occurances = cp.deepcopy(list_occurances) 
    while list_occurances_item in temp_occurances:
            temp_occurances.remove(list_occurances_item)  

    return temp_occurances

print("current list (of numbers after removing 1): ", remove_all_occurances_if_item_found(list_numbers, 1))
print("current list (of numbers after removing 3): ", remove_all_occurances_if_item_found(list_numbers, 3))
print("current list (of numbers after removing 5): ", remove_all_occurances_if_item_found(list_numbers, 5))

        
    





