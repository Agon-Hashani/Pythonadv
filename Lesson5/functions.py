def greet():
    print("Hello World!")

greet()

def greet_person(name):
     print("Hello", name)

greet_person("Agon")


def greet_person1(name, greeting= "Hello"):
    message = f'{greeting}, {name}'
    return message

default_greeting = greet_person1("Alice")

custom_greeting = greet_person1("Bob", "Hi")

print(default_greeting)
print(custom_greeting)

greeting = "Hello"

def greet1(name):
    message = f"{greeting}, {name}"
    print(message)

    greet1("Bob")
    print(greeting)



def greet2(name):
    message = f"Hello, {name}"
    print(message)

greet2("Alice")

# print(message)

def greet3(name):
    global  message
    message = f"{greeting}, {name}"
    print(message)

greet3("Bob")
print(message)


message = f"{greeting}, Student!"
print(message)

