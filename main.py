""" Code Principal """

FILENAME = "listes.csv"
SEPARATOR = ';'

#### Fonctions secondaires

def read_data(filename):
    """
    Retourne le contenu du fichier <filename> sous forme d'une liste de listes d'entiers.

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 liste par ligne, avec des entiers)
    """
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            return [list(map(int, line.strip().split(SEPARATOR))) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Erreur : le fichier {filename} n'a pas été trouvé.")
        return []
    except ValueError:
        print("Erreur : le fichier contient des données non valides.")
        return []

def get_list_k(data, k):
    """
    Retourne la k-ième liste de la liste de listes.

    Args:
        data (list): liste de listes
        k (int): index de la liste à retourner

    Returns:
        list: la k-ième liste
    """
    if 0 <= k < len(data):
        return data[k]
    print(f"Erreur : l'indice {k} est hors des limites.")
    return None

def get_first(l):
    """
    Retourne le premier élément d'une liste.

    Args:
        l (list): une liste

    Returns:
        int: le premier élément de la liste
    """
    if l:
        return l[0]
    print("Erreur : la liste est vide.")
    return None

def get_last(l):
    """
    Retourne le dernier élément d'une liste.

    Args:
        l (list): une liste

    Returns:
        int: le dernier élément de la liste
    """
    if l:
        return l[-1]
    print("Erreur : la liste est vide.")
    return None

def get_max(l):
    """
    Retourne le maximum d'une liste.

    Args:
        l (list): une liste

    Returns:
        int: le maximum de la liste
    """
    if l:
        return max(l)
    print("Erreur : la liste est vide.")
    return None

def get_min(l):
    """
    Retourne le minimum d'une liste.

    Args:
        l (list): une liste

    Returns:
        int: le minimum de la liste
    """
    if l:
        return min(l)
    print("Erreur : la liste est vide.")
    return None

def get_sum(l):
    """
    Retourne la somme des éléments d'une liste.

    Args:
        l (list): une liste

    Returns:
        int: la somme des éléments de la liste
    """
    if l:
        return sum(l)
    print("Erreur : la liste est vide.")
    return 0

#### Fonction principale

def main():
    """
    Fonction principale qui teste les fonctions secondaires.
    """
    data = read_data(FILENAME)
    if not data:
        print("Aucune donnée disponible.")
        return

    print(f"Données lues depuis {FILENAME} : {data}")

    k = 1
    liste_k = get_list_k(data, k)
    if liste_k is not None:
        print(f"Liste à l'index {k} : {liste_k}")

    if data:
        sample_list = data[0]
        print(f"Première liste : {sample_list}")
        print(f"Premier élément : {get_first(sample_list)}")
        print(f"Dernier élément : {get_last(sample_list)}")
        print(f"Maximum : {get_max(sample_list)}")
        print(f"Minimum : {get_min(sample_list)}")
        print(f"Somme : {get_sum(sample_list)}")

if __name__ == "__main__":
    main()
