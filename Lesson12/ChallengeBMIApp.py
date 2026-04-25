from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age, weight, height):
        self._name = name
        self._age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be positive")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Adult(Person):

    def calculate_bmi(self):
        return self._weight / (self._height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Weight: {self._weight} kg")
        print(f"Height: {self._height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")


class Child(Person):

    def calculate_bmi(self):
        return (self._weight / (self._height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Weight: {self._weight} kg")
        print(f"Height: {self._height} m")
        print(f"BMI (adjusted): {bmi:.2f}")
        print(f"Category: {category}")


class BMIApp:
    def __init__(self):
        self.people_list = []

    def add_person(self):
        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if age < 18:
            person = Child(name, age, weight, height)
        else:
            person = Adult(name, age, weight, height)

        self.people_list.append(person)
        print(f"{name} added successfully!\n")

    def print_results(self):
        if not self.people_list:
            print("No people in the list.\n")
            return

        print("\n" + "=" * 50)
        print("BMI RESULTS FOR ALL PEOPLE")
        print("=" * 50 + "\n")

        for i, person in enumerate(self.people_list, 1):
            print(f"Person {i}:")
            person.print_info()
            print()

    def run(self):
        print("Welcome to BMI Calculator!")
        print("=" * 50 + "\n")

        while True:
            print("Options:")
            print("1. Add a person")
            print("2. Print BMI results")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                self.add_person()
            elif choice == "2":
                self.print_results()
            elif choice == "3":
                print("Thank you for using BMI Calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    app = BMIApp()
    app.run()