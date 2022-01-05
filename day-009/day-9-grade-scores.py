student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Rafael": 0,
    "Dereck": -7,
    "Karen": 110
}

#TODO-1 Create an empty dictionary student_grades

student_grades = {}

for key in student_scores:
    print(key, student_scores[key])
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fails"

print(student_grades)