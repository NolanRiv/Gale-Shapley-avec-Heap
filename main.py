from gale_shapley_matching.src.utils import load_data
from gale_shapley_matching.src.heap import generate_student_permutations
from gale_shapley_matching.src.gale_shapley import gale_shapley
from gale_shapley_matching.src.matching import compare_matchings, save_results_to_csv, save_results_to_json

def main():
    # Chemins des fichiers
    universities_file = "./gale_shapley_matching/data/universities.csv"
    students_file = "./gale_shapley_matching/data/students.csv"
    output_csv = "./gale_shapley_matching/data/results.csv"
    output_json = "./gale_shapley_matching/data/best_result.json"

    # Charger les données
    universities = load_data(universities_file)
    students = load_data(students_file)

    # Vérifier les données chargées
    if not universities:
        print(f"Erreur : Aucun université n'a été chargée depuis {universities_file}.")
        return
    if not students:
        print(f"Erreur : Aucun étudiant n'a été chargé depuis {students_file}.")
        return

    # Vérification du contenu
    print(f"Universités chargées : {universities}")
    print(f"Étudiants chargés : {students}")

    # Générer les permutations pour l'étudiant 1
    try:
        student1_preferences = students[0]["preferences"]
    except IndexError:
        print("Erreur : La liste des étudiants est vide ou invalide.")
        return

    student1_permutations = generate_student_permutations(student1_preferences)

    # Appliquer Gale-Shapley à chaque permutation
    all_matchings = []
    all_scores = []

    for perm in student1_permutations:
        # Mettre à jour les préférences de l'étudiant 1 pour cette permutation
        students[0]["preferences"] = perm
        # Exécuter l'algorithme de Gale-Shapley
        matching, score = gale_shapley(universities, students, student1_permutations)
        all_matchings.append(matching)
        all_scores.append(score)

    # Analyser les résultats
    best_result = compare_matchings(student1_permutations, all_matchings, all_scores)

    # Afficher le meilleur appariement
    print("Meilleure permutation et appariement:")
    print("Permutation:", best_result["best_permutation"])
    print("Matching:", best_result["best_matching"])
    print("Score de l'étudiant 1:", best_result["best_score"])

    # Sauvegarder les résultats
    save_results_to_csv(output_csv, student1_permutations, all_matchings, all_scores)
    save_results_to_json(output_json, best_result)
    print(f"Résultats sauvegardés dans {output_csv} et {output_json}")

if __name__ == "__main__":
    main()
