from datetime import datetime 
import numpy as np


###################
# Conversion date #
###################

# Fonction qui permet de transformer les dates en format datetime

def transfo_dates_directe(liste):
    for i in range(len(liste)):
        liste[i] = transformation_date_locale(liste[i])
    return liste

# Fonction permettant d'associer une valeur exploitable à notre date (Non utilisée finalement)

def transformation_date_globale(tableau_entree):
    for i in range(len(tableau_entree)):
        for j in range(len(tableau_entree[i])):
            date = tableau_entree[i][j][1]
            format_date = "%d/%m/%y"
            tableau_entree[i][j][1] = datetime.strptime(date, format_date).date()
    return tableau_entree

# Fonction permettant d'associer une valeur exploitable à nos heures de début et fin (Non utilisée finalement)

def transformation_heure(tableau_entree):
    for i in range(len(tableau_entree)):
        for j in range(len(tableau_entree[i])):
            heure_debut = tableau_entree[i][j][2]
            heure_fin = tableau_entree[i][j][3]
            format_heure = "%H:%M"
            tableau_entree[i][j][2] = datetime.strptime(heure_debut, format_heure).time()
            tableau_entree[i][j][3] = datetime.strptime(heure_fin, format_heure).time()
    return tableau_entree

# Fonction permettant de changer la date en donnée exploitable afin de comparer le fichier utilisateur avec les dates des sports (Utile dans l'extraction de la base de donnée)

def transformation_date_locale(data): 
    format_date = "%d/%m/%y"
    date = datetime.strptime(data, format_date).date()
    return date




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

#############################################
# Fonction auxiliaire tranformation tableau #
#############################################

# Cette fonction va permettre de transformer l'écriture d'un tableau afin que l'exploitation de ses données soit plus facile par la suite (C'est juste la transposée d'une matrice n*n globalement)

def transposee(tab):
    return np.transpose(tab)

# Cette fonction permet d'ajouter des cases à nos rencontres

def add_info(l):
    rep = l
    for i in range(0,len(l)):
        for j in range(0, len(l[i])):
            rep[i][j].append("")
    return rep

##########################
# Fonction test présence #
##########################

def is_in(pays,sport):
    rep=False
    for i in range(len(sport)):
        if pays==sport[i]:
            rep=True
    return rep

"""is_in("AUS",tennis)"""


def is_in2(nation,sport):
    rep=False
    if sport in sport:
        for j in range(5):
            if nation==sport[j]:
                rep=True
    return rep


#################################
# Fonctions évaluation distance #
#################################

###########################################################
#fonction pour convertir un angle degré décimaux en radian#
###########################################################

import numpy as np
def convert(d):
    return d*np.pi/180

##################################################################
#fonction qui calcule la distance entre 2 lieux (à vol d'oiseaux)#
##################################################################

def distanceAB(latA,longA,latB,longB):
    latA = convert(latA)
    longA = convert(longA)
    latB = convert(latB)
    longB = convert(longB)
    RT = 6378137          # rayon de la Terre
    angle = np.acos(np.sin(latA)*np.sin(latB) + np.cos(latA)*np.cos(latB)*np.cos(abs(longB-longA)))
    return angle*RT  #en mètre


 