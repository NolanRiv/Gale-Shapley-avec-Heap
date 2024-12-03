import csv
import json

def compare_matchings(permutations, matchings, scores):
    """
    Compare les appariements obtenus pour chaque permutation.
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
    """
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Permutation", "Matching", "Score"])
        for perm, match, score in zip(permutations, matchings, scores):
            writer.writerow([perm, match, score])


def save_results_to_json(file_name, results):
    """
    Sauvegarde les résultats dans un fichier JSON.
    """
    with open(file_name, mode="w") as file:
        json.dump(results, file, indent=4)