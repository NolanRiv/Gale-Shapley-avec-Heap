def gale_shapley(universities, students, student_permutations):
    """
    Implémentation de l'algorithme de Gale-Shapley avec les permutations des préférences de l'étudiant 1.
    """
    best_matching = None
    best_score = float("inf")

    for perm in student_permutations:
        students[0]["preferences"] = perm
        original_preferences = students[0]["preferences"]

        proposals = {university['name']: [] for university in universities}
        matched_students = {student['name']: None for student in students}
        unmatched_universities = list(universities)

        # Algorithme de Gale-Shapley
        while unmatched_universities:
            university = unmatched_universities.pop(0)
            for student_name in university['preferences']:
                if student_name not in proposals[university['name']]:
                    proposals[university['name']].append(student_name)
                    student = next(s for s in students if s['name'] == student_name)
                    if matched_students[student_name] is None:
                        matched_students[student_name] = university['name']
                        break
                    else:
                        current_match = matched_students[student_name]

                        student_preferences = next(s for s in students if s['name'] == student_name)['preferences']

                        if university['name'] not in student_preferences or current_match not in student_preferences:
                            print(f"Error: {university['name']} or {current_match} not found in preferences for {student_name}")
                            continue

                        if student_preferences.index(university['name']) < student_preferences.index(current_match):
                            matched_students[student_name] = university['name']
                            unmatched_universities.append(next(u for u in universities if u['name'] == current_match))
                        break
            else:
                unmatched_universities.append(university)

            # Calculer le "score" pour l'étudiant 1
            university_for_student1 = matched_students[students[0]['name']]

            if university_for_student1 is None:
                # Si l'étudiant 1 n'a pas été apparié, donner un score très élevé
                score = float("inf")
            else:
                # Vérifier si l'université appariée est dans les préférences de l'étudiant
                if university_for_student1 in students[0]['preferences']:
                    score = students[0]['preferences'].index(university_for_student1)
                else:
                    # Si l'université appariée n'est pas dans les préférences, donner un score élevé
                    score = float("inf")

            # Si cette permutation donne un meilleur score pour l'étudiant 1, on la garde
            if score < best_score:
                best_score = score
                best_matching = matched_students.copy()

            students[0]['preferences'] = original_preferences

    return best_matching, best_score