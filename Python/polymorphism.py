class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")

t1 = Teacher()
t1.get_designation()

class Product():
    def get_product(self):
        print("Base Product")

class Pen():
    def get_product(self):
        print("Product Pen")


pen = Pen()
pen.get_product()