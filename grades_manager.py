def get_students(student_grades, keys):
    result = {}

    for name in keys:
        found = False
        for student in student_grades:
            if student.lower() == name.lower():
                result[student] = student_grades[student]
                found = True
                break

        if not found:
            print(f"{name.title()} not found!")

    return result