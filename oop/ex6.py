class Demo:

    # instance method
    def show(self):
        print("This is instance method")

    # class method
    @classmethod
    def display(cls):
        print("This is class method")

    # static method
    @staticmethod
    def info():
        print("This is static method")

# creating object
d1 = Demo()

# calling methods
d1.show()        # instance method
Demo.display()   # class method
Demo.info()      # static method