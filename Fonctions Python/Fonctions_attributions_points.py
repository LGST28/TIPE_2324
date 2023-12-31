#################################################
# Attribution des points en fonction de la date #
#################################################

from Fonctions_de_création import transformation_date_locale
from datetime import datetime, timedelta
from Fonctions_utiles import transfo_dates_directe, add_info, is_in2
from Centre_de_commande import indice_points, indice_date_rencontre, points_dates_larges, points_dates_strictes, dates_utilisateur, dates_larges, jours_ajouts, points_nationalité, points_finale, points_demi, points_quart



# On transfome les dates utilisateur (entrée) en données exploitables

dates_utilisateur = transfo_dates_directe(dates_utilisateur)

# On ajoute un delta de jours pour les dates plus larges

if dates_utilisateur[0] is not None and dates_utilisateur[1] is not None:
    dates_larges[0] = dates_utilisateur[0] + timedelta(days=jours_ajouts)
    dates_larges[1] = dates_utilisateur[1] - timedelta(days=jours_ajouts)


# Désormais nous avons deux informations, les dates de l'utilisateur, et les dates ± un delta que l'on peut définir 

# Pour l'instant, on suppose que l'on a pas attribué tous les

def add_points_date_global(liste):
    
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            # On attribue les points dans le cas des dates strictes
            if dates_utilisateur[1] <= transformation_date_locale((liste[i][j][indice_date_rencontre])) <= dates_utilisateur[0]:
                if (len(liste[i][j]) < indice_points+1): # Dans le cas où l'on a pas déjà ajouté de la place pour les points, on le fait là
                    add_info(liste) # Maintenant on a de la place 
                # Désormais on attribue les points associés aux dates strictes
                n_p_attribution_simple(liste[i][j], points_dates_strictes , indice_points) # Fonction attribuant les bons points

            if (dates_larges[1] <= transformation_date_locale(liste[i][j][indice_date_rencontre]) < dates_utilisateur[1]) or (dates_utilisateur[0] < transformation_date_locale(liste[i][j][indice_date_rencontre]) <= dates_larges[0]):
                if (len(liste[i][j]) < indice_points+1): # Dans le cas où l'on a pas déjà ajouté de la place pour les points, on le fait là
                    add_info(liste) # Maintenant on a de la place 
                n_p_attribution_simple(liste[i][j], points_dates_larges , indice_points)

    return liste                


#########################
# Attribution de points #
#########################

def attribuer_points(tab,val):
    
    y=tab[indice_points]
    tab[indice_points]=val+y
    return tab


def n_p_attribution_simple(seq,n, indice):
    seq[indice] = n
    return seq


def n_p_ajout_point_globale(liste, n):
    l_rep = liste
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            l_rep[i][j][indice_points] = n
    return l_rep
                


############
# Critères #
############

def pts_pour_type(t):
    if(t[0]=="Finale"):
        attribuer_points(t,points_finale)
    if(t[0]=='Demi finale'):
        attribuer_points(t,points_demi)
    if(t[0]=='Quart de finale'):
        attribuer_points(t,points_quart)
    return t



"""print(pts_pour_type(t[0]))
print(pts_pour_type(t[1]))
print(pts_pour_type(t[2]))"""


########################################################
# Fonction critère sport en fonction de la nationalité #
########################################################

from Base_de_données import sports
from Fonctions_utiles import is_in


def pts_pour_nationalité (nationalité,t):
    sport=sports.pays_prefs[t[0]]
    if is_in(nationalité,sport) :
        attribuer_points(t,points_nationalité)
    return t




#print(rencontres)


################################
# Fonctions pour les distances #
################################

from Fonctions_utiles import distanceAB

# l'utilisateur à le choix entre déplacement limité, déplacement modéré, déplacement illimité

def pts_pour_distance(type_de_deplacement,t1,t2):
    latA=t1[7][0]
    longA=t1[7][1]
    latB=t2[7][0]
    longB=t2[7][1]
    distance = distanceAB(latA,longA,latB,longB)
    if(type_de_deplacement=="peu de déplacement"):
        if(distance<2000):
            attribuer_points(t1,2)
            attribuer_points(t2,2)
    if (type_de_deplacement=="déplacement modéré"):
        if(distance<8000):
            attribuer_points(t1,2)
            attribuer_points(t2,2)
    return t1,t2



#############################################################
# Fonction qui donne des points aux pays favoris par sports #
#############################################################



def pts_pour_favoris (t):
    if (is_in2(t[3][0],t[0][0])==True) :
        attribuer_points(t,5)
    if (is_in2(t[4][0],t[0][0])==True) :
        attribuer_points(t,5)
    return t
