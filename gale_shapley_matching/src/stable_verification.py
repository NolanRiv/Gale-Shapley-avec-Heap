def is_stable_matching(universities, students, best_perm, best_matching):
    """
        Vérifie si le matching obtenu pour la meilleure permutation est bien stable.
    """
    students[0]["preferences"] = best_perm

    university_preferences = {u['name']: u['preferences'] for u in universities}
    student_preferences = {s['name']: s['preferences'] for s in students}

    university_matching = {v: k for k, v in best_matching.items()}

    for student, university in best_matching.items():
        for preferred_university in student_preferences[student]:
            if preferred_university == university:
                break  

            current_student = university_matching.get(preferred_university)
            if current_student is None or \
               university_preferences[preferred_university].index(student) < university_preferences[preferred_university].index(current_student):
                print(f"Instable: {student} et {preferred_university} préfèrent être ensemble.")
                return False

        for preferred_student in university_preferences[university]:
            if preferred_student == student:
                break 
            
            current_university = best_matching.get(preferred_student)
            if current_university is None or \
               student_preferences[preferred_student].index(university) < student_preferences[preferred_student].index(current_university):
                print(f"Instable: {university} et {preferred_student} préfèrent être ensemble.")
                return False

    print("L'appariement est stable.")
    return True
