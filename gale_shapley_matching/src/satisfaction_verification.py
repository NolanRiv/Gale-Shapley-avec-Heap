def calculate_satisfaction(universities, students, matching):
    """
    Calcule les taux de satisfaction des étudiants, des universités, et global.
    """
    num_universities = len(universities)
    num_students = len(students)

    # Préférences des étudiants et des universités sous forme de dictionnaire
    student_preferences = {s['name']: s['preferences'] for s in students}
    university_preferences = {u['name']: u['preferences'] for u in universities}

    # Satisfaction des étudiants
    student_satisfaction = 0
    for student, university in matching.items():
        rank = student_preferences[student].index(university) + 1
        student_satisfaction += 1 - (rank - 1) / num_universities
    student_satisfaction /= num_students

    # Satisfaction des universités
    university_satisfaction = 0
    for university in university_preferences:
        accepted_students = [student for student, uni in matching.items() if uni == university]
        if accepted_students:
            satisfaction = 0
            for student in accepted_students:
                rank = university_preferences[university].index(student) + 1
                satisfaction += 1 - (rank - 1) / num_students
            university_satisfaction += satisfaction / len(accepted_students)
    university_satisfaction /= num_universities

    # Satisfaction globale
    global_satisfaction = (student_satisfaction + university_satisfaction) / 2

    return {
    "student_satisfaction": f"{student_satisfaction * 100:.2f}%",
    "university_satisfaction": f"{university_satisfaction * 100:.2f}%",
    "global_satisfaction": f"{global_satisfaction * 100:.2f}%",
}