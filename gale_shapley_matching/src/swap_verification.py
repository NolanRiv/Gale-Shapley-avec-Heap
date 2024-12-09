
from gale_shapley_matching.src.stable_verification import is_stable_after_swaps

def iterative_swap_optimization(universities, students, matching):
    student_preferences = {s['name']: s['preferences'] for s in students}
    swaps_applied = True

    while swaps_applied:
        swaps_applied = False
        student_names = list(matching.keys())

        for i in range(len(student_names)):
            for j in range(i + 1, len(student_names)):
                student1 = student_names[i]
                student2 = student_names[j]

                university1 = matching[student1]
                university2 = matching[student2]

                current_rank1 = student_preferences[student1].index(university1)
                current_rank2 = student_preferences[student2].index(university2)

                new_rank1 = student_preferences[student1].index(university2)
                new_rank2 = student_preferences[student2].index(university1)

                # Vérifier si le swap améliore
                if new_rank1 < current_rank1 and new_rank2 < current_rank2:
                    # Appliquer le swap temporairement
                    matching[student1], matching[student2] = university2, university1

                    # Vérifier si le nouvel appariement est stable
                    is_stable, _ = is_stable_after_swaps(universities, students, matching)

                    if is_stable:
                        swaps_applied = True
                        print(f"Échange stable effectué : {student1} ↔ {student2}")
                    else:
                        # Annuler le swap si instable
                        matching[student1], matching[student2] = university1, university2
                        print(f"Échange annulé (instable) : {student1} ↔ {student2}")
                    
                    break
            if swaps_applied:
                break

    print("Optimisation terminée.")
    return matching