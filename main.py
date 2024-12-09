import time
from gale_shapley_matching.src.utils import load_data
from gale_shapley_matching.src.heap import generate_student_permutations
from gale_shapley_matching.src.gale_shapley import gale_shapley
from gale_shapley_matching.src.matching import compare_matchings, save_results_to_csv, save_results_to_json
from gale_shapley_matching.src.stable_verification import is_stable_matching, is_stable_after_swaps
from gale_shapley_matching.src.generate_data import generate_data
from gale_shapley_matching.src.swap_verification import iterative_swap_optimization
from gale_shapley_matching.src.satisfaction_verification import calculate_satisfaction

def main():

    num_cases = 5

    generate_data(num_universities=num_cases, num_students=num_cases, universities_file='./gale_shapley_matching/data/universities.csv', students_file='./gale_shapley_matching/data/students.csv')

    # Chemins des fichiers
    universities_file = "./gale_shapley_matching/data/universities.csv"
    students_file = "./gale_shapley_matching/data/students.csv"
    output_csv = "./gale_shapley_matching/data/results.csv"
    output_json = "./gale_shapley_matching/data/best_result.json"


    start_total = time.time()

    # Charger les données
    start_load = time.time()
    universities = load_data(universities_file)
    students = load_data(students_file)
    end_load = time.time()

    # Générer les permutations pour l'étudiant 1
    try:
        student1_preferences = students[0]["preferences"]
    except IndexError:
        print("Erreur : La liste des étudiants est vide ou invalide.")
        return

    start_permutations = time.time()
    student1_permutations = generate_student_permutations(student1_preferences)
    end_permutations = time.time()

    # Contenir les résultats de chaque permutations
    all_matchings = []
    all_scores = []

    # Stocker la préférence sincère
    original_preferences = students[0]["preferences"]

    # Tester toutes les permutations pour l'étudiant 1 et les sauvegarde
    start_gs = time.time()
    for perm in student1_permutations:
        students[0]["preferences"] = perm
        matching, score = gale_shapley(universities, students, original_preferences, perm)
        all_matchings.append(matching)
        all_scores.append(score)
    end_gs = time.time()

    # Analyser les résultats
    start_compare = time.time()
    best_result = compare_matchings(student1_permutations, all_matchings, all_scores)
    end_compare = time.time()

    # Vérifie la stabilité du meilleur résultat obtenu
    start_stability = time.time()
    if(is_stable_matching(universities, students, best_result["best_permutation"], best_result["best_matching"])):

        # Afficher le meilleur appariement
        print("Meilleure permutation et appariement:")
        print("Permutation:", best_result["best_permutation"])
        print("Matching:", best_result["best_matching"])
        print("Score de l'étudiant 1:", best_result["best_score"])

        # Sauvegarder les résultats
        save_results_to_csv(output_csv, student1_permutations, all_matchings, all_scores)
        save_results_to_json(output_json, best_result)
        print(f"Résultats sauvegardés dans {output_csv} et {output_json}")

    else:
        print("La meilleure permutation trouvée est instable")
    print("------------------------------------------------------------------------------")


    end_stability = time.time()

    end_total = time.time()

    print(f"Temps de chargement des données : {end_load - start_load:.2f} s")
    print(f"Temps de création des permutations : {end_permutations - start_permutations:.2f} s")
    print(f"Temps de Gale-Shapley : {end_gs - start_gs:.2f} s")
    print(f"Temps de comparaison des résultats : {end_compare - start_compare:.2f} s")
    print(f"Temps de vérification stabilité : {end_stability - start_stability:.2f} s")
    print(f"Temps Total : {end_total - start_total:.2f} s")
    print("------------------------------------------------------------------------------")

    optimized_matching = iterative_swap_optimization(universities, students, best_result["best_matching"].copy())
    is_stable, blocking_pairs = is_stable_after_swaps(universities, students, optimized_matching)

    if is_stable:
        print("Appariement avant optimisation :", best_result["best_matching"])
        print("Appariement final stable :", optimized_matching)
    else:
        print("Appariement final instable. Paires bloquantes :", blocking_pairs)
    print("------------------------------------------------------------------------------")

    before_satisfaction = calculate_satisfaction(universities, students, best_result["best_matching"])
    print("Satisfaction avant optimisation:")
    print(f"- Étudiants : {before_satisfaction['student_satisfaction']}")
    print(f"- Universités : {before_satisfaction['university_satisfaction']}")
    print(f"- Globale : {before_satisfaction['global_satisfaction']}")

    after_satisfaction = calculate_satisfaction(universities, students, optimized_matching)
    print("\nSatisfaction après optimisation:")
    print(f"- Étudiants : {after_satisfaction['student_satisfaction']}")
    print(f"- Universités : {after_satisfaction['university_satisfaction']}")
    print(f"- Globale : {after_satisfaction['global_satisfaction']}")
    print("------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()