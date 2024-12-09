import csv
import random
import os

def generate_data(num_universities, num_students, universities_file, students_file):

    # Liste des étudiants avec leurs noms et préférences (initialement vides)
    students = []
    for i in range(num_students):
        student_name = f"Student{i+1}"
        students.append({'id': i + 1, 'name': student_name, 'preferences': []})

    # Liste des universités
    universities = []
    for i in range(num_universities):
        university_name = f"University{i+1}"
        universities.append({'id': i + 1, 'name': university_name, 'preferences': []})

    # Générer les préférences des étudiants (ordre aléatoire des universités)
    for student in students:
        student_preferences = random.sample([university['name'] for university in universities], len(universities))
        student['preferences'] = student_preferences

    # Générer les préférences des universités (ordre aléatoire des étudiants)
    for university in universities:
        university_preferences = random.sample([student['name'] for student in students], len(students))
        university['preferences'] = university_preferences

    # Sauvegarder les données des étudiants dans un fichier CSV
    with open(students_file, mode='w', newline='') as stu_file:
        writer = csv.writer(stu_file)
        writer.writerow(['id', 'name', 'preferences'])
        for student in students:
            # Convertir la liste des préférences en chaîne de caractères formatée
            writer.writerow([student['id'], student['name'], student['preferences']])

    # Sauvegarder les données des universités dans un fichier CSV
    with open(universities_file, mode='w', newline='') as uni_file:
        writer = csv.writer(uni_file)
        writer.writerow(['id', 'name', 'preferences'])
        for university in universities:
            # Convertir la liste des préférences en chaîne de caractères formatée
            writer.writerow([university['id'], university['name'], university['preferences']])

    print(f"Données générées et sauvegardées dans {students_file} et {universities_file}.")
    print("------------------------------------------------------------------------------")
