class Employee:
    start_time = "10am"
    end_time = "6pm"


class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary = salary

accountant1 = Accountant(25_000, "Accountant")

print(accountant1.salary, accountant1.role, accountant1.start_time, accountant1.end_time)

class Teacher:
    def __init__(self,salary):
        self.salary = salary


class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TA(Teacher, Student):
    def __init__(self, salary, cgpa, name):
        super().__init__(salary)
        Student.__init__(self, cgpa)
        self.name = name


ta1 = TA(15_000, 3.2, "Abc")

print(ta1.name, ta1.salary, ta1.cgpa)