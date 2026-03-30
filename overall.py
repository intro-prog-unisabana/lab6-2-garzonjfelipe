def student_averages(students):
    result = {}
    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)
    return result

def assignment_averages(students):
    result = {}

    for grades in students.values():
        for hw, score in grades.items():
            if hw not in result:
                result[hw] = []
            result[hw].append(score)

    for hw in result:
        result[hw] = round(sum(result[hw]) / len(result[hw]))

    return result