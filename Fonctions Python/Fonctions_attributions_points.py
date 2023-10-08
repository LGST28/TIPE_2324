#################################################
# Attribution des points en fonction de la date #
#################################################

# On récupère les dates de l'utilisateur dans le fichier création 

from Fonctions_de_création import lire_donnee, transformation_date, creation_donnees, indice_points, add_info, indice_points, n_p_attribution_simple
from datetime import datetime, timedelta

dates_utilisateur = lire_donnee(r"/Users/lg/Library/CloudStorage/OneDrive-Personnel/Prépa/Sup/TIPE/information_utilisateur_double.csv")[0]

# Points à attriber

points_strictes = 1
points_larges = 0

indice_date_rencontre = 1

# Fonction qui permet de transformer les dates en format datetime

def transfo_dates_directe(liste):
    for i in range(len(liste)):
        liste[i] = transformation_date(liste[i])
    return liste

'''def conversion_datetime(date_str):
    try:
        # Tentez de convertir la date en datetime si elle n'est pas déjà au format datetime
        if not isinstance(date_str, datetime):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')  # Ajustez le format de la date selon vos besoins
        else:
            date_obj = date_str  # Si c'est déjà un datetime, laissez-le tel quel
        return date_obj
    except ValueError:
        return None  # Si la conversion échoue, renvoyez None ou gérez l'erreur de votre choix
    '''

# Faire attention, pour l'instant les dates sont inversées, avec le retour en premier (indice 0)

dates_larges = [0, 0]

# Maintenant, vous pouvez ajouter 2 jours à la première date et soustraire 2 jours à la deuxième date

dates_utilisateur = transfo_dates_directe(dates_utilisateur)

if dates_utilisateur[0] is not None and dates_utilisateur[1] is not None:
    dates_larges[0] = dates_utilisateur[0] + timedelta(days=2)
    dates_larges[1] = dates_utilisateur[1] - timedelta(days=2)



print(dates_utilisateur)
print("")
print([dates_larges])

# Désormais nous avons deux informations, les dates de l'utilisateur, et les dates ± un delta que l'on peut définir 

# Pour l'instant, on suppose que l'on a pas attribué tous les

def add_points_date_global(liste):
    
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            # On attribue les points dans le cas des dates strictes
            if dates_utilisateur[1] <= transformation_date((liste[i][j][indice_date_rencontre])) <= dates_utilisateur[0]:
                if (len(liste[i][j]) < indice_points+1): # Dans le cas où l'on a pas déjà ajouté de la place pour les points, on le fait là
                    add_info(liste) # Maintenant on a de la place 
                # Désormais on attribue les points associés aux dates strictes
                n_p_attribution_simple(liste[i][j], points_strictes , indice_points) # Fonction attribuant les bons points

            if (dates_larges[1] <= transformation_date(liste[i][j][indice_date_rencontre]) < dates_utilisateur[1]) or (dates_utilisateur[0] < transformation_date(liste[i][j][indice_date_rencontre]) <= dates_larges[0]):
                if (len(liste[i][j]) < indice_points+1): # Dans le cas où l'on a pas déjà ajouté de la place pour les points, on le fait là
                    add_info(liste) # Maintenant on a de la place 
                n_p_attribution_simple(liste[i][j], points_larges , indice_points)

    return liste

print()

donnees = creation_donnees()


test = add_points_date_global(donnees)

for tab in test:
    for sous_tab in tab:
        print(sous_tab)
                
                
                




#print(rencontres)