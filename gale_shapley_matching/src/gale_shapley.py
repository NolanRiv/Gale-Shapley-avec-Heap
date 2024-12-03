def gale_shapley(universities, students, original_preferences, perm):
    """
    Implémentation de l'algorithme de Gale-Shapley avec une permutation spécifique des préférences de l'étudiant 1.
    """
    # Remplace la permutation originel par la nouvelle 
    students[0]["preferences"] = perm

    # Stock les propositions faites aux étudiants, si ses derniers sont appariés et les universités n'ayant encore aucun match
    proposals = {university['name']: [] for university in universities}
    matched_students = {student['name']: None for student in students}
    unmatched_universities = list(universities)

    # Algorithme de Gale-Shapley
    while unmatched_universities:
        # Récupère la première université sans match 
        university = unmatched_universities.pop(0)
        for student_name in university['preferences']:
            if student_name not in proposals[university['name']]:
                # Fais une proposition au premier dans la liste de préférences qui n'en a pas déjà reçu une
                proposals[university['name']].append(student_name)
                student = next(s for s in students if s['name'] == student_name)
                # Verifie si l'étudiant à déjà un match
                if matched_students[student_name] is None:
                    # Sinon créer le match
                    matched_students[student_name] = university['name']
                    break
                else:
                    current_match = matched_students[student_name]

                    student_preferences = next(s for s in students if s['name'] == student_name)['preferences']
                    # Verifie si m'université est dans la liste de préférences
                    if university['name'] not in student_preferences or current_match not in student_preferences:
                        print(f"Error: {university['name']} or {current_match} not found in preferences for {student_name}")
                        continue

                    # Si oui vérifie si la nouvelle université est plus haute dans ses préférences et remplace le match
                    if student_preferences.index(university['name']) < student_preferences.index(current_match):
                        matched_students[student_name] = university['name']
                        unmatched_universities.append(next(u for u in universities if u['name'] == current_match))
                    break
        # Sinon rajoute l'université à la liste de celles sans match
        else:
            unmatched_universities.append(university)

    # Match automatiquement le dernier étudiant et la dernière université ensemble
    unmatched_students = [student for student, university in matched_students.items() if university is None]
    remaining_universities = [university['name'] for university in universities if university['name'] not in matched_students.values()]
    for student_name, university_name in zip(unmatched_students, remaining_universities):
        matched_students[student_name] = university_name

    # Calculer le "score" pour l'étudiant 1 après l'algorithme
    university_for_student1 = matched_students[students[0]['name']]

    best_score = float("inf")
    best_matching = None

    # Score = Position de l'université dans la liste sincère (0 = meilleur résultat | 4 = pire)
    if university_for_student1 in original_preferences:
        best_score = original_preferences.index(university_for_student1)
        best_matching = matched_students.copy()

    return best_matching, best_score