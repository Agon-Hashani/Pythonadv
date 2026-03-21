class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


st1 = Student("Alice",15, "DigitalSchool" )
st2 = Student("Bob", 17, "DigitalSchool")

print(st1.course)
print(st2.course)
