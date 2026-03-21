def cal_area(length, width):
    return length * width

def cal_perimeter(length, width):
    return 2 * (length + width)

length = 5
width = 3

area = cal_area(length, width)
perimeter = cal_perimeter(length, width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")