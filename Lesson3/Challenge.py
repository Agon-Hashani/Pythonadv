s_gpa = 4.5
s_score = 75

if s_gpa >= 3.5:
    if 50 <= s_score <= 65:
        print(f"Student with GPA {s_gpa} and test score of {s_score} may be eligible for partial "
              f"scholarship.")
    elif s_score > 65:
        print(f"Student with GPA {s_gpa} and test score of {s_score} is eligible for a full scholarship.")
    else:
        print(f"Student with GPA {s_gpa} and test score of {s_score} is not eligible for a scholarship")
else:
    print(f"Student with GPA {s_gpa} and test score of {s_score} is not eligible for a scholarship")