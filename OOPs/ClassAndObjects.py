class Student:
    def __init__(self, fn, ln, age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

s1 = Student("Soumen", "Maji", "24")
s2 = Student("Name", "Title", "Age")

print(s1.firstName, s1.lastName, s1.age)
print(s2.firstName, s2.lastName, s2.age)
