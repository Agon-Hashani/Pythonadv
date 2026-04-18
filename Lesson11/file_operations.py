# file_path = "example"
# file = open(file_path)
#
#
# content = file.read()
# print(content)
#
# file.close()

import os

with open('example', 'r')as file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()

with open("example", "w")as file:
    file.write("Amiri nuk po shkruan kod po rrin në telefon")


lines = ["Amiri edhe Noart shkruan shum shpejt\n", "Erjoni edhe Germanium hajn shum haribo"]

with open("example", 'w') as file:
    file.writelines(lines)