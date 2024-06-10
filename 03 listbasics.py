#empty list 
marks : list = []
print(marks)

#change marks
marks = [80, 90, 100, 70, 80]
print(marks)

#access elements 
print("First element: ", marks[0])
print("Second Element: ", marks[1])
print("Third Element: ", marks[2])
print("Fourth Element: ", marks[3])
print("Fifth Element: ", marks[4])

#print("Sixth Element: ", marks[5])
marks = [80, 90, 100, 70, 80, 90]
print("Sixth Element: ", marks[5])

#make a list of multiples of 5 from 1 to 50
#[5, 10, 15, 20, ..., 50]
#??? what's the logic? 
multiples_of_5 = []
print("Before adding item in the list: ",multiples_of_5)
 
for i in range(0, 51, 5):
    if i == 0:
        continue
    
    multiples_of_5.append(i)
 
#dynamism 
marks = [80, 90, 100, 70, 80, 90, 99.9]
print(marks)

hotel_names = ["hotel paradise", "hotel sunrise", 1454]
print(hotel_names)