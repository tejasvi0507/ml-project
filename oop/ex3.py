class Mobile:
    def set_details(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m1 = Mobile()
m1.set_details("Samsung", 20000)
m1.show_details()