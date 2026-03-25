# Parent class
class Animal:
    def sound(self):
        print("Animals make sound")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# creating object
d1 = Dog()

# calling methods
d1.sound()   # from parent class
d1.bark()    # from child class