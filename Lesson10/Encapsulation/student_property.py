class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def get_age(self):
        return self.__age

    @age.setter
    def set_age(self, age):
        self.__age = age

student1 = Student("Alice", 17)

print("Name: ", student1.name)
print("Age: ", student1.age)

student1.name = "Bob"
student1.age = 19

print("Updated Name: ", stdent1.name)
print("Updated Age: ", stdent1.age)

