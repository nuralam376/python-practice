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