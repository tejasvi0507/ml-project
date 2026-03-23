class Student:
    school = "ABC School"   # class variable

    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks    # instance variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School:", Student.school)

# creating objects
s1 = Student("Tejasvi", 90)
s2 = Student("Rahul", 85)

s1.display()
print("-----")
s2.display()