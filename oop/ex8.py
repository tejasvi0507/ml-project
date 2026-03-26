class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

s1 = Student("Tejasvi", 90)
s1.show()