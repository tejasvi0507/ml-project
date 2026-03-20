class Student:
    def set_data(self, name, marks):
        self.name = name
        self.marks = marks

    def show_data(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student()
s1.set_data("Tejasvi", 90)
s1.show_data()