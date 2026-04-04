class Student:
    def __init__(self,name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

std1 = Student("Abc", 3.58)
std2 = Student("Def", 3.76)

print(f"{std1.name} has a cgpa of {std1.cgpa}")
print(f"{std2.name} has a cgpa of {std2.cgpa}")

class College: 
    name = "Abc College"

    def __init__(self, name):
        self.name = name

clg1 = College("Def")

print(clg1.name)
print(College.name)

class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    def get_info(self): 
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @classmethod
    def get_storage_type(cls):
        print(f"Storage Type = {cls.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"Final Price = {final_price}")

laptop1 = Laptop("16GB", "256GB")

laptop1.get_info()
laptop1.get_storage_type()
Laptop.get_storage_type()
Laptop.calc_discount(40_000, 10)

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
    
    def get_info(self):
        print(f"Price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total Products = {cls.count}")

    @staticmethod
    def get_discount(price, discount):
        finalPrice = price - (price * discount / 100)
        print(f"Final Price after discount = {finalPrice}")


product1 = Product("Laptop", 50_000)
product2 = Product("Mobile", 10_000)
product3 = Product("Pen", 10)

product1.get_info()
product2.get_info()
product3.get_info()
Product.get_count()
Product.get_discount(product1.price, 10)