students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50], 
    ["Mary", 35, 40, 30], 
    ["John", 65, 70, 68],
    ["Precious", 80, 90, 76]
    ]

for student in students:
    name = student[0]
    total_score = 0
    score_count = 0
    for i in range(1, len(student)):
        total_score += student[i]
        score_count += 1
    average = total_score / score_count

    if average >= 70:
        grade = "A"
        print(f"{name}- Average: {round(average, 2)} - Grade: {grade}")
    elif average >= 60:
        grade = "B"
        print(f"{name}- Average: {round(average, 2)} - Grade: {grade}")
    elif average >= 50:
        grade = "C"
        print(f"{name}- Average: {round(average, 2)} - Grade: {grade}")
    elif average >= 45:
        grade = "D"
        print(f"{name}- Average: {round(average, 2)} - Grade: {grade}")
    elif average >= 40:
        grade = "E"
        print(f"{name}- Average: {round(average, 2)} - Grade: {grade}")
    else:
        grade = "F"
        print(f"{name}- Average: {round(average, 2)} - Grade: {grade}")
