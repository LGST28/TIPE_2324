from datetime import datetime


# Ce fichier contient une fonction qui, sur base de l'entrée de différente plage horaire va retourner les sessions auxquelles l'utilisateur va pouvoir participer, sur base de la première valide #

tableau_entree = [["Badminton", "Double", "Type d'activité", "28/05/23", "08:30", "13:00", "Cour Chanzy" ],
                  ["Badminton", "Double", "Type d'activité", "27/05/23", "15:30", "18:00", "Cour Chanzy" ],
                  ["Badminton", "Double", "Type d'activité", "27/05/23", "07:30", "15:00", "Cour Chanzy" ],
                  ["Badminton", "Simple", "Type d'activité", "28/05/23", "18:30", "19:00", "Cour Chanzy" ],
                  ["Football", "None", "Type d'activité", "24/05/23", "06:30", "10:00", "Cour Chanzy" ],
                  ["Badminton", "Simple", "Type d'activité", "27/05/23", "05:30", "15:00", "Cour Chanzy" ],
                  ["Football", "None", "Type d'activité", "29/05/23", "08:30", "19:00", "Cour Chanzy" ],
                  ["Badminton", "Double", "Type d'activité", "27/05/23", "08:30", "13:00", "Cour Chanzy" ]]


# Fonction permettant d'associer une valeur exploitable à notre date

def transformation_date(tableau_entree):
    for i in range(len(tableau_entree)):
        date = tableau_entree[i][3]
        format_date = "%d/%m/%y"
        tableau_entree[i][3] = datetime.strptime(date, format_date).date()
    return tableau_entree


# Fonction permettant d'associer une valeur exploitable à nos heures de début et fin

def transformation_heure(tableau_entree):
    for i in range(len(tableau_entree)):
        heure_debut = tableau_entree[i][4]
        format_heure = "%H:%M"
        tableau_entree[i][4] = datetime.strptime(heure_debut, format_heure).time()
        heure_fin = tableau_entree[i][5]
        tableau_entree[i][5] = datetime.strptime(heure_fin, format_heure).time()
    return tableau_entree


# Dictionnaire pour le tri du tableau 
    
def cle_tri(element):
    sport = element[0]
    ss_sport = element[1]
    date = element[3]
    heure_debut = element[4]
    return (sport, ss_sport, date, heure_debut)

# Fonction qui utilise ce dictionnaire pour trier notre tableau

def tri_croissant(tableau):
    tableau = sorted(tableau, key=cle_tri)
    return tableau
    
# Fonction qui permet de supprimer toutes les superpositions d'horaires
    
def ejection(tableau):
    i = 0
    while i < len(tableau)-1:
        if tableau[i][0] == tableau[i+1][0] and tableau[i][1] == tableau[i+1][1] and tableau[i][3] == tableau[i+1][3]:
            if (tableau[i][5]) > tableau[i+1][4]:
                del tableau[i+1]
            else:
                i += 1
        else:
            i += 1
    return tableau
    
# On applique nos fonctions de tri à notre tableau d'entrée

tableau = transformation_heure(transformation_date(tableau_entree))

# Tri du tableau dans l'ordre croissant

tableau_croissant = tri_croissant(tableau)

# Ejection des superpositions

tableau_final = ejection(tableau_croissant)

# On imprime les sous tableaux les uns sous les autres

for sous_tableau in tableau_final:
    print(sous_tableau)
    print()