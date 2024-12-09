def is_stable_matching(universities, students, best_perm, best_matching):
    """
        Vérifie si le matching obtenu pour la meilleure permutation est bien stable.
    """
    students[0]["preferences"] = best_perm

    university_preferences = {u['name']: u['preferences'] for u in universities}
    student_preferences = {s['name']: s['preferences'] for s in students}

    # Inverse le matching pour obtenir l'appariement du coté des universités
    university_matching = {v: k for k, v in best_matching.items()}

    for student, university in best_matching.items():
        for preferred_university in student_preferences[student]:
            if preferred_university == university:
                break  

            # Vérifie si l'université et un autre étudiant se préfèrent l'un l'autre
            current_student = university_matching.get(preferred_university)
            if current_student is None or \
               university_preferences[preferred_university].index(student) < university_preferences[preferred_university].index(current_student):
                print(f"Instable: {student} et {preferred_university} préfèrent être ensemble.")
                return False

        for preferred_student in university_preferences[university]:
            if preferred_student == student:
                break 
            
            # Vérifie si l'étudiant et une autre université se préférent l'un l'autre
            current_university = best_matching.get(preferred_student)
            if current_university is None or \
               student_preferences[preferred_student].index(university) < student_preferences[preferred_student].index(current_university):
                print(f"Instable: {university} et {preferred_student} préfèrent être ensemble.")
                return False

    print("L'appariement est stable.")
    return True

def is_stable_after_swaps(universities, students, matching):
    """
    Vérifie la stabilité de l'appariement après les swaps.
    """
    blocking_pairs = []

    # Convertir les préférences en dictionnaires pour un accès rapide
    student_preferences = {s['name']: s['preferences'] for s in students}
    university_preferences = {u['name']: u['preferences'] for u in universities}

    # Vérifier chaque étudiant et université
    for student, current_university in matching.items():
        # Obtenir les préférences actuelles de l'étudiant et de son université
        student_pref_list = student_preferences[student]
        current_rank_student = student_pref_list.index(current_university)

        for preferred_university in student_pref_list[:current_rank_student]:
            # Vérifier si l'université préfère cet étudiant à son partenaire actuel
            university_pref_list = university_preferences[preferred_university]
            current_partner = next(
                (s for s, u in matching.items() if u == preferred_university),
                None
            )

            # Vérifier les rangs dans les préférences de l'université
            student_rank_in_university = university_pref_list.index(student)
            current_partner_rank_in_university = (
                university_pref_list.index(current_partner) if current_partner else float('inf')
            )

            # Si l'université préfère cet étudiant et cet étudiant préfère cette université, c'est une paire bloquante
            if student_rank_in_university < current_partner_rank_in_university:
                blocking_pairs.append((student, preferred_university))

    return len(blocking_pairs) == 0, blocking_pairs