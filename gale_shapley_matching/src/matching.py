import csv
import json

def compare_matchings(permutations, matchings, scores):
    """
    Compare les appariements obtenus pour chaque permutation.
    
    Parameters:
        permutations (list): Liste des permutations des préférences de l'étudiant 1.
        matchings (list): Liste des appariements correspondants.
        scores (list): Liste des scores associés pour l'étudiant 1.
    
    Returns:
        dict: Détails de la permutation et de l'appariement ayant donné le meilleur score.
    """
    best_index = scores.index(min(scores))  # Trouver l'indice du meilleur score
    return {
        "best_permutation": permutations[best_index],
        "best_matching": matchings[best_index],
        "best_score": scores[best_index]
    }


def save_results_to_csv(file_name, permutations, matchings, scores):
    """
    Sauvegarde les résultats dans un fichier CSV.
    
    Parameters:
        file_name (str): Nom du fichier CSV.
        permutations (list): Liste des permutations des préférences de l'étudiant 1.
        matchings (list): Liste des appariements correspondants.
        scores (list): Liste des scores associés pour l'étudiant 1.
    """
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Permutation", "Matching", "Score"])
        for perm, match, score in zip(permutations, matchings, scores):
            writer.writerow([perm, match, score])


def save_results_to_json(file_name, results):
    """
    Sauvegarde les résultats dans un fichier JSON.
    
    Parameters:
        file_name (str): Nom du fichier JSON.
        results (dict): Dictionnaire contenant les résultats.
    """
    with open(file_name, mode="w") as file:
        json.dump(results, file, indent=4)


if __name__ == "__main__":
    # Exemple de données simulées
    permutations = [
        ["UniversityA", "UniversityB", "UniversityC"],
        ["UniversityB", "UniversityA", "UniversityC"],
        ["UniversityC", "UniversityB", "UniversityA"]
    ]
    matchings = [
        {"student1": "UniversityA", "student2": "UniversityB", "student3": "UniversityC"},
        {"student1": "UniversityB", "student2": "UniversityA", "student3": "UniversityC"},
        {"student1": "UniversityC", "student2": "UniversityA", "student3": "UniversityB"}
    ]
    scores = [0, 1, 2]  # Exemple de scores pour l'étudiant 1
    
    # Comparer les résultats
    best_result = compare_matchings(permutations, matchings, scores)
    print("Meilleure permutation et appariement:", best_result)
    
    # Sauvegarder les résultats
    save_results_to_csv("../data/results.csv", permutations, matchings, scores)
    save_results_to_json("../data/results.json", best_result)
