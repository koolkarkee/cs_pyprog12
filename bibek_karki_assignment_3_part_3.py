#26 Create a class Rectangle containing instance variables length and breadth. The class also
# contains two instance methods area() and perimeter() to find area and perimeter of rectangles
# respectively. Use this class to find area and perimeter of two different rectangles.

class Rectangle:
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth 

    def get_area(self):
        return self.length * self.breadth
 
    def get_perimeter(self):
        return 2*(self.length + self.breadth)
    
    def show_area(self):
        print(f"The area of the rectangle is {self.get_area()} square units")

    def show_perimeter(self):
        print(f"The perimeter of the rectangle is {self.get_perimeter()} units") 

rect1 = Rectangle(2, 4)
rect2 = Rectangle(5, 10)

rect1.show_area()
rect1.show_perimeter()
rect2.show_area()
rect2.show_perimeter()
print("--------------------------------")

#27. Create a class Circle containing an instance variable radius. The class also contains two
# instance methods area() and circumference() to find area and circumference of circles
# respectively. Use this class to find area and circumference of two different circles. Use PI as a
# class variable.

import math
class Circle:
    PI = math.pi

    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return Circle.PI * (self.radius ** 2)

    def show_area(self): 
        print(f"The area of the circle is : {self.get_area()} square units")

    def get_circumference(self):
        return Circle.PI * 2 * self.radius

    def show_circumference(self): 
        print(f"The circumference of the circle is {self.get_circumference()}")

circ1 = Circle(7)
circ2 = Circle(14)
circ1.show_area()
circ1.show_circumference()
circ2.show_area()
circ2.show_circumference()

print("--------------------------------")

#28. Create a class Box with instance variables width, height and depth. The class also contains
# instance methods volume() and surface_area() to find volume and surface area of boxes
# respectively. Use this class to find volume and surface area of two different boxes.

class Box:
    def __init__(self, width, height, depth) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def get_volume(self):
        return self.width * self.height * self.depth 

    def show_volume(self): 
        print(f"The volume of the box is {self.get_volume()} cubic units")

    def get_surface_area(self):
        return 2* (self.width * self.height + self.height * self.depth + self.width * self. depth)

    def show_surface_area(self):  
        print(f"The surface area of the box is {self.get_surface_area()} square units")

box1 = Box(1, 2, 3)
box2 = Box(5, 10 ,15)
box1.show_volume()
box1.show_surface_area()
box2.show_volume()
box2. show_surface_area()

print("--------------------------------")

# 29. Create a class Time with three instance variables hours, minutes, and seconds. Add instance
# methods display() to display the time in hh:mm:ss format and add() to add two time objects.
# Use this class to add and display two different time objects.
class Time:
    def __init__(self, hours, minutes, seconds) -> None: 
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        if hours >= 24 or hours <= 0:
            self.hours = 0
        
        if minutes <= 0 or minutes >= 60:
            self.minutes = 0
            
        if seconds <= 0 or seconds >= 60:
            self.seconds = 0

    def display(self):
        hours = f"{self.hours}"
        minutes = f"{self.minutes}"
        seconds = f"{self.seconds}" 

        if self.hours < 10:
            hours = f"0{hours}" 
        if self.minutes < 10:
            minutes = f"0{minutes}" 
        if self.seconds < 10:
            seconds = f"0{seconds}"  
        
        print(f"{hours}:{minutes}:{seconds}")  

    def add(self, t1, t2):  
        t3 = Time(0, 0, 0)  
        second_carry = 0
        minute_carry = 0

        if t1.seconds + t2.seconds >= 60:  
            second_carry = 1
            t3.seconds = t1.seconds + t2.seconds - 60 
        else:
            t3.seconds = t1.seconds + t2.seconds  

        if t1.minutes + t2.minutes >= 60: 
            minute_carry = 1
            t3.minutes = t1.minutes + t2.minutes + second_carry - 60 
        else:
            t3.minutes = t1.minutes + t2.minutes  + second_carry
            if t3.minutes >= 60:
                minute_carry = 1
                t3.minutes = t3.minutes - 60

        if t1.hours + t2.hours >= 24:
            t3.hours = t1.hours + t2.hours + minute_carry - 24 
        else:
            t3.hours = t3.hours + minute_carry
            if t3.hours >= 24:
                t3.hours = t3.hours - 24

        return t3

t1 = Time(23, 59, 59)
t1.display()
t2 = Time(23, 59, 59)
t2.display()

#adding two time objects and displaying the output 
t3 = t2.add(t1, t2)
t3.display()

print("--------------------------------")

# 30 Create a class Distance containing instance variables feet and inches. The class also contains
# instance methods add() and compare() to add and compare two distance objects respectively.
# Use this class to create two different distance objects and add and compare these two distance
# objects.
class Distance:
    def __init__(self, feet, inch) -> None:
        self.feet = feet
        self.inch = inch 

        if inch >= 12 or inch < 0:
            self.inch = 0
        
        if feet < 0:
            self.feet = 0 

    def add(self, d1, d2):
        d3 = Distance(0, 0)
        inch_carry = 0

        if d1.inch + d2.inch >= 12:
            inch_carry = 1
        
        d3.inch = d1.inch + d2.inch - 12
        d3.feet = d1.feet + d2.feet + inch_carry 

        return d3

    def compare(self, d1, d2):
        d1_total = d1.feet * 12 + d1.inch
        d2_total = d2.feet * 12 + d2.inch

        if d1_total > d2_total:
            print(f"{d1.feet} foot and {d1.inch} inches is greater than {d2.feet} foot and {d2.inch} inches")
        elif d1_total < d2_total:
            print(f"{d2.feet} foot and {d2.inch} inches is greater than {d1.feet} foot and {d1.inch} inches")
        elif d1_total == d2_total:
            print(f"Both are equal")

    def display(self):
        print(f"{self.feet} foot and {self.inch} inches")

d1 = Distance(4, 11)
d1.display()
d2 = Distance(5, 11)
d2.display()

d3 = d2.add(d1, d2) 
print(f"Sum after adding two distances :") 
d3.display()
d3.compare(d1, d2) 

print("--------------------------------")

# 31. Create a class Student with instance variables name, roll_number, and marks in five subjects.
# Add three instance methods in this class to calculate total(), percentage(), and division() of the
# marks obtained by the students. Use this class to find total marks obtained, percentage, and
# division of five students.
class Student: 
    def __init__(self, name: str, roll_number: int, marks: list) -> None:
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  

    def total(self):
        sum = 0
        for i in range(0, len(self.marks)):
            sum += self.marks[i]
         
        return sum
    
    def percentage(self):
        return Student.total(self)/5
    
    def division(self):
        percent = Student.percentage(self)
        div = ""

        if percent >= 80:
            div = "Distinction"
        elif percent >= 70 and percent < 80:
            div = "First  Division"
        elif percent >= 60 and percent < 70:
            div = "Second Division"
        elif percent >= 40 and percent < 60:
            div = "third division"
        elif percent < 40:
            div = "Failed"  

        #failed condition check for individual subject
        for i in range(0, len(self.marks)):
            if self.marks[i] < 40:
                div = "Failed"
        
        return div

student1 = Student("Ram", 12, [50, 60, 70, 80, 90])
student2 = Student("Shyam", 12, [60, 60, 70, 80, 90])
student3 = Student("Hari", 12, [80, 85, 50, 80, 90])
student4 = Student("Gita", 12, [90, 60, 70, 50, 90])
student5 = Student("Sita", 12, [100, 100, 95, 100, 35])

students = [student1, student2, student3, student4, student5] 
for i in range(0, len(students)):
    print("--------------------------------")
    print(f"Student details :")
    print(f"Name : {students[i].name} | Roll number : {students[i].roll_number}")
    print(f"Total Marks : {students[i].total()}")
    print(f"Percentage : {students[i].percentage()}")
    print(f"Division : {students[i].division()}") 
    print("--------------------------------")


# 32. Create a parent class Bonus with instance variables sales_id and sales_amount. Add get_bonus
# method that calculates a salesperson’s bonus using the foumula bonus = sales * 0.05. Create a
# child class named PremiumBonus from Bonus. The child class’s get_premium_bonus()
# method should calculate the bonus using the formula bonus = sales * 0.05 + (sales – 2500) *
# 0.01. Now, create an object of PremiumBonus class and use this object to find both bonus and
# premium bonus.

class Bonus:
    def __init__(self, sales_id, sales_amount) -> None:
        self.sales_id = sales_id
        self.sales_amount = sales_amount

    def get_bonus(self):
        return self.sales_amount * 0.05
    

class PremiumBonus(Bonus):
    def __init__(self, sales_id, sales_amount) -> None:
        Bonus.__init__(self, sales_id, sales_amount)

    def get_premium_bonus(self):
        return (self.sales_amount * 0.05 + (self.sales_amount - 2500) * 0.01)

premium_bonus = PremiumBonus(2300, 25000)
print(f"Bonus amount : {premium_bonus.get_bonus()}")
print(f"Premium Bonus: {premium_bonus.get_premium_bonus()}")
print("--------------------------------") 
