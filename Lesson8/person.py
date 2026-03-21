class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def greet(self):
            print(f"Hello,i am {self.name}, and I am {self.age} years old.")


per1 = Person("Alice",15)
per2 = Person("Bob", 17)

per1.greet()
per2.greet