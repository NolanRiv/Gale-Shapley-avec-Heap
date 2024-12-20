import csv
import ast

def load_data(file_path):
    """
    Charge les données d'un fichier CSV et les formate en une liste de dictionnaires.
    """
    data = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convertie les préférences de chaîne de caractères en liste d'entiers
                row["preferences"] = ast.literal_eval(row["preferences"])
                row["name"] = str(row["name"])
                row["id"] = int(row["id"])
                data.append(row)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
    return data
