try:
    result = 10/0
except ZeroDivisionError:
    print("Oops! Tride to divide by zero.")


fruits = {
    "appls": 5,
    "banana": 7,
    "orange": 3
}
try:
    print(fruits["Cherry"])
except KeyError:
    print("The key does not exists in the List ")




text = "This is not a number"

try:
    trxt_to_int = int(text)
except Exception as e:
    print("An error occurred while parsing data: ", e)

try:
    result = 10/2
except ZeroDivisionError:
    print("Division by Zero error occurred")
else:
    print("Division successful. Result: ", result)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by Zero error occurred")
finally:
    print("Finally block executed")

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division: ", result)
    except ZeroDivisionError:
        print("Invalid division by zero")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print(f"Unexpected error: {e}")


        divide_numbers(10,2)
        divide_numbers(10,0)
        divide_numbers(10,'2' )