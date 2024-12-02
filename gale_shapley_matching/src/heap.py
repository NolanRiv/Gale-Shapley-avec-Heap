def heap_permutation(arr, n, result, original_pref):
    """
    Algorithme des permutations de Heap
    La première permutation sera toujours l'originelle (sincère).
    
    Paramètres:
        arr (list): Une liste de préférences.
        n (int): La longueur de la liste de préférences.
        result (list): La liste stockant toutes les permutations.
        original_pref (list): La liste sincère.
    """
    if n == 1:
        result.append(arr[:])
    else:
        for i in range(n):
            # Recursively generate permutations for the first n-1 elements
            heap_permutation(arr, n - 1, result, original_pref)
            
            # Swap the elements depending on whether n is odd or even
            if n % 2 == 1:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]  # Swap first and last element
            else:
                arr[i], arr[n - 1] = arr[n - 1], arr[i]  # Swap ith and last element

    # Ensure that the first permutation in the list is the original preference
    if not result:
        result.append(original_pref[:])  # Append the original preference first
    else:
        result[0] = original_pref[:]  # Ensure the first permutation is the original one


def generate_student_permutations(student_preferences):
    """
    Génère toutes les permutation des préférences de l'étudiant 
    
    Paramètres:
        student_preferences (list): Liste des universités par ordre de préférences de l'étudiant.
    
    Returns:
        list: Liste de toutes les permutations pour les préférences de l'étudiant.
    """
    result = []
    original_pref = student_preferences[:]
    heap_permutation(student_preferences, len(student_preferences), result, original_pref)
    return result


if __name__ == "__main__":
    # Example: Let's say the first student's preferences are for three universities
    student1_preferences = ["UniversityA", "UniversityB", "UniversityC", "UniversityD", "UniversityE"]
    
    # Generate permutations
    permutations = generate_student_permutations(student1_preferences)
    
    # Print all permutations
    for perm in permutations:
        print(perm)
    
    # Verify the number of permutations
    print(f"\nTotal permutations: {len(permutations)} (should be {len(student1_preferences)}!)")
