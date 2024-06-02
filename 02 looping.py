#for i in range(start = 1, end = 10, steps = 1):
for i in range(1, 11, 1):
    print(i) 

print("-----------------------")

for i in range(2, 101, 2):
    print(i) 

print("-----------------------")

for i in range(5, 101, 5):
    print(i)

print("-----------------------")

#table of 2 
#2*1 = 2
#2*2 = 4

for i in range(0, 10, 1):
    n =  2
    print(f"{n} * {i+1} = {n * (i + 1)}") 

print("-------------------------------")
#while loop demo
count = 0
while count < 10:
    n = 2
    print(f"{n} * {count + 1} = {n * (count + 1)}")
    count += 1
else:
    print("value of count = ", count) 