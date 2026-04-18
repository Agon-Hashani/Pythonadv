class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age


student1 = Student('Alice', 17)

print("Name: ", student1.get_name())

stdent1.set_name('Bob')
print("Updated Name: ", stdent1.get_name())

print("Age: ", stdent1.get_age())

stdent1.set_age(18)
print("Updated age: ", stdent1.get_age())