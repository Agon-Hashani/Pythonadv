name = ["Alice", 'Bob', 'Charlie', "David"]

for name in name:
    print(name)

for number in range(1, 6):
        print(number)

        number = [12, 45, 6, 72, 21, 8, 94, 57]

        maximum = number[0]

        for num in number:
            if num > maximum:
                maximum = num
print("This is maximum value in the list: ", maximum)

count = 1

while count <= 5:
    print("Iteration", count)
    count += 1

    numbers = [1, 2, 3, 4, 5, 6]
    target = 4


    for number in numbers:
        print(number)
        if number == target:
            print("Target found!")
            break

scores = [68, 42, 57, 78, 35, 62, 50, 92]
total = 0
count = 0

for score in scores:
    if score < 50:
        continue

    total += score
    count += 1

avg = total / count if count > 0 else 0

print("Average score for scores above 50: ", avg)


while True:
    user_input = input("Enter a positive number: ")

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break

    print("Invalid input. Please try again.")

print("You entered a valid positive number: ", number)