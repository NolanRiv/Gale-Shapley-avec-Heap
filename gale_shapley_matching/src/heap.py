def heap_permutation(arr, n, result, original_pref):
    """
    Algorithme des permutations de Heap
    La première permutation sera toujours l'originelle (sincère).
    """
    if n == 1:
        result.append(arr[:])
    else:
        for i in range(n):
            # Génère les permutations à partir de la liste sincère
            heap_permutation(arr, n - 1, result, original_pref)
            
            # Inverse les éléments selon pair/impair
            if n % 2 == 1:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]  # Swap le premier et le dernier
            else:
                arr[i], arr[n - 1] = arr[n - 1], arr[i]  # Swap le ith et le dernier

    # Assure que la liste sincère soit toujours en première
    if not result:
        result.append(original_pref[:])  # Sinon l'ajoute
    else:
        result[0] = original_pref[:]


def generate_student_permutations(student_preferences):
    """
    Génère toutes les permutation des préférences de l'étudiant 
    """
    result = []
    original_pref = student_preferences[:]
    heap_permutation(student_preferences, len(student_preferences), result, original_pref)
    return result
