with open('example', 'r')as file:
   for line in file:
       cleaned_line = line.strip()
       print(cleaned_line)

with open('example', 'r') as file:
    for line in file:
        words = line.strip().split()
        print(words)

name = "Alice"
age = 30

with open('output.txt', 'w')as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")

with open('output.txt', 'w')as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

with open('example', 'r')as infile, open('output.txt', 'w')as outfile:
    for line in infile:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("Line 1", "Line 2")
        outfile.write(modified_line + "\n")