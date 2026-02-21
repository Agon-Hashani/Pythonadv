greads = {
    ("John", "Math"):  5,
    ("Alice", "Biology"): 4,
    ("Bob", "Physics"): 3.5,
    ("Eve", "Music"): 5,
    ("John", "English"):4
}

print("John's grade in math is", greads[("John", "Math")])

greads[("Bob", "Math")] = 3
print(greads)