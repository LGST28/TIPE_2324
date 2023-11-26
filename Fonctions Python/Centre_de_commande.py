##############
# Librairies #
##############

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import copy
from Fonctions_de_création import creation_donnees, lire_donnee
#from Fonctions_attributions_points import n_p_ajout_point_globale # Cet appel à la fonction cause l'erreur
from Fonctions_utiles import add_info, is_in, distanceAB
from Base_de_données import *
from Fonctions_de_tri import *


dossier_racine = r"/Users/lg/Library/CloudStorage/OneDrive-Personnel/Prépa/Spé/TIPE/TIPE_2324/"

##################################
# Import de fonctions provisoire #
##################################

# Voici ici les fonctions qui sont dans d'autres fichiers mais qu'on ne peux pas appeler

def n_p_ajout_point_globale(liste, n):
    l_rep = liste
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            l_rep[i][j][indice_points] = n
    return l_rep


def attribuer_points(tab,val):
    
    y=tab[indice_points]
    tab[indice_points]=val+y
    return tab


def pts_pour_type(t):
    if(t[indice_type]=="Finale"):
        attribuer_points(t,points_finale)
    if(t[indice_type]=='Demi finale'):
        attribuer_points(t,points_demi)
    if(t[indice_type]=='Quart de finale'):
        attribuer_points(t,points_quart)
    return t

def pts_pour_nationalité (nationalité,t):
    sport=sports[t[0]]
    if is_in(nationalité,sport) :
        attribuer_points(t,points_nationalité)
    return t

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


#######################
# Nouvelles fonctions #
#######################

# On commence par attribuer les points en fonction du type de rencontre

def fct_points_type_rencontres(tab): # Fonction qui attribue à chaque rencontre les points associés au type de rencontre
    rep = []
    for i in range (len(tab)): # Ici nous avons chaque sport et on travaille sur les rencontres
        for j in range (len(tab[i])):
            rep.append(pts_pour_type(tab[i][j]))
    return rep

def fct_points_nationalite(tab): # Fonction qui attribue les points à chaque rencontre en fonction de la nationalité
    rep = []
    for i in range (len(tab)): # Ici nous avons chaque sport et on travaille sur les rencontres
            rep.append(pts_pour_nationalité("Chine",tab[i]))
    return rep

"""
test = fct_points_type_rencontres(l_sports_av_points_0)

print(test)

test_2 = fct_points_nationalite(test)


print()
print()
print()

print(test_2)


print()
print()
print()

"""



###################################
# Structure des données utilisées #
###################################

# Pour l'instant, voici le modèle que nous utilisons, ce dernier sera étoffé au fur et à mesure

modele=[[[],[],[],[],[]]]   #| Indice 0 : Nom du sport
                            #| Indice 1 : Date
                            #| Indice 2 : Heure de début
                            #| Indice 3 : Heure de fin
                            #| Indice 4 : Sous-sport
                            #| Indice 5 : Description de l'évènement 
                            #| Indice 6 : Pays
                            #| Indice 7 : Ville 
                            #| Indice 8 : Poids
                            #| Indice 9 : Type de rencontre (Si nécessaire)



##############################
# Base de données temporaire #
##############################

liste_evn     = [[["badminton" , "27/07/2024" , "08:30"	, "12:00" , "Arena Porte de La Chapelle" , "Poules préliminaires"] , 
                  ["badminton" , "27/07/2024" , "14:30"	, "17:00" , "Arena Porte de La Chapelle" , "Finale"] , 
                  ["badminton" , "27/07/2024" , "19:30"	, "21:00" , "Arena Porte de La Chapelle" , "Demi finale"] , 
                  ["badminton" , "28/07/2024" , "08:30"	, "12:00" , "Arena Porte de La Chapelle" , "Demi finale"] , 
                  ["badminton" , "28/07/2024" , "14:30"	, "17:00" , "Arena Porte de La Chapelle" , "Quart de finale"] , 
                  ["badminton" , "28/07/2024" , "19:30"	, "21:00" , "Arena Porte de La Chapelle" , "Finale"] ,
                  ["badminton" , "29/07/2024" , "08:30"	, "12:00" , "Arena Porte de La Chapelle" , "Poules préliminaires"] , 
                  ["badminton" , "29/07/2024" , "14:30"	, "17:00" , "Arena Porte de La Chapelle" , "Finale"] , 
                  ["badminton" , "29/07/2024" , "19:30"	, "21:00" , "Arena Porte de La Chapelle" , "Demi finale"] , 
                  ["badminton" , "30/07/2024" , "08:30"	, "12:00" , "Arena Porte de La Chapelle" , "Demi finale"] , 
                  ["badminton" , "30/07/2024" , "14:30"	, "17:00" , "Arena Porte de La Chapelle" , "Quart de finale"] , 
                  ["badminton" , "30/07/2024" , "19:30"	, "21:00" , "Arena Porte de La Chapelle" , "Finale"]
                    ] ,
                 [
                  ["football" , "27/07/2024" , "08:30"	, "12:00" , "Arena Porte de La Chapelle" , "Poules préliminaires"] , 
                  ["football" , "27/07/2024" , "14:30"	, "17:00" , "Arena Porte de La Chapelle" , "Finale"] , 
                  ["football" , "27/07/2024" , "19:30"	, "21:00" , "Arena Porte de La Chapelle" , "Demi finale"] , 
                  ["football" , "28/07/2024" , "08:30"	, "12:00" , "Arena Porte de La Chapelle" , "Demi finale"] , 
                  ["football" , "28/07/2024" , "14:30"	, "17:00" , "Arena Porte de La Chapelle" , "Quart de finale"] , 
                  ["football" , "28/07/2024" , "19:30"	, "21:00" , "Arena Porte de La Chapelle" , "Finale"]

                    
                 ]]

################################
# Informations sur les indices #
################################

indice_date_rencontre = 1
indice_points = 6
indice_type = 5

##############################
# Informations sur les dates #
##############################

# Faire attention, pour l'instant les dates sont inversées, avec le retour en premier (indice 0)

dates_larges = [0, 0] # Ici il suffit d'initialiser la liste à 0 car les dates seront ajoutées automatiquement
jours_ajouts = 1

###############################
# Informations sur les points #
###############################

points_dates_strictes = 1
points_dates_larges = 0
points_nationalité = 2
points_finale = 5
points_demi = 3
points_quart = 1 

############################
# Informations utilisateur #
############################

dates_utilisateur = lire_donnee(dossier_racine+r"/information_utilisateur_double.csv")[0]
# Faire attention, pour l'instant les dates sont inversées, avec le retour en premier (indice 0)
 

################################
# Poste de contrôle du contenu #
################################

base_de_donnee = 1

tableau_final = 1

##############################################
# Poste de commande de l'appel des fonctions #
##############################################

# On créé notre tableau avec tous les sports auxquels l'utilisateur peut assister 

l_sports = liste_evn # On créé la liste de toutes les rencontres auxquelles ont peut assister
l_sports_av_points = add_info(l_sports) # On ajoute la possibilité d'attribuer des points

def creation_simu (l_sports_av_points_0):
    l_sports_av_points_0 = n_p_ajout_point_globale(l_sports_av_points,0) # On met tous les points à 0.
    l_sports_av_points_type = fct_points_type_rencontres(l_sports_av_points_0)
    l_sports_av_points_pays = fct_points_nationalite(l_sports_av_points_type)
    return l_sports_av_points_pays



##################################################################################
# Création de la fonction qui fait varier les points et qui sotcke les résultats #
##################################################################################

tab_simu_1 = []
liste = l_sports_av_points
for i in range (0,5):  # Dans la première boucle on fait varier les points pour la naitonalité de l'utilisateur 
    points_nationalité = i
    
    for j in range (0,2): # Dans les deux prochaines boucles on fait varier les points pour les dates

        for k in range(j , j + 3) : # Ici les dates strictes
            
            points_dates_larges = j
            points_dates_strictes = k
            
            for l in range (0,3) : # Dans les 3 boucles suivantes on fait varier les points associés au type de rencontre

                for m in range (l, l+2):

                    for n in range (m, m+3): 

                        points_quart = l 
                        points_demi = m
                        points_finale = n

                    tab_simu_1.append(creation_simu(liste))
                    
                    
                    
                    """print()
                    print('i : ',i)
                    print('j : ',j)
                    print('k : ',k)
                    print('l : ',l)
                    print('m : ',m)
                    print('n : ',n)"""
                    

print(tab_simu_1)




















"""

######################
# Zone de recherches #
######################



#print(tab_points_type_1)


# Désormais nous avons accès à un tableau sur lequel nous pouvons travailler les points

# On créé un tableau qui va contenir chacune de nos simulations
# Les simulations 1 représentent l'application des fonctions date -> points -> dates

#simu_tab_1 = []

# Les simulations 2 représentent l'application des fonctions points -> dates

simu_tab_2 = []

# On fait des boucles qui font varier les paramètres des points, et pour chaque boucle on va récupérer le tableau de sortie, et donc le tableau proposé

def tri_simu_1(liste) :

    rep = ejection_globale_n(liste)
    rep = tri_tableau(rep,indice_points)
    rep = ejection_globale_n(rep)

    return rep

def tri_simu_2(liste) :

    rep = tri_tableau(liste,indice_points)


    rep = ejection_globale_n(rep)

    return rep


print()
print()
print("Observons désormais la différence entre les différents tris que nous pouvons faire")
print()
print()

simu_tab_1 = tri_simu_1(l_sports_av_points_pays)

for sport in simu_tab_1:
    print(sport)

print()
print()
print("Et désormais que ce passe-t-il lorsque nous changeons la manière de trier les données ?")
print()
print()


simu_tab_2 = tri_simu_2(l_sports_av_points_pays)

for sport in simu_tab_2:
    print(sport)

print()
print() """











########################################
# Poste de contrôle de la présentation #
########################################

def bleu(texte): # Permet d'imprimer une chaine de caractère en bleu
    print('\033[94m' + texte + '\033[0m')
def vert(texte): # Permet d'imprimer une chaine de caractère en vert
    print('\033[92m' + texte + '\033[0m')
def rouge(texte): # Permet d'imprimer une chaine de caractère en rouge
    print('\033[91m' + texte + '\033[0m')    
def gras(texte): # Permet d'imprimer une chaine de caractère en gras
    print('\033[1m' + texte + '\033[0m') 
def italique(texte): # Permet d'imprimer une chaine de caractère en italique
    print('\033[3m' + texte + '\033[0m')
def souligne(texte): # Permet d'imprimer une chaine de caractère en souligné
    print('\033[4m' + texte + '\033[0m')
def bleu_gras(texte): # Permet d'imprimer une chaine de caractère en bleu et en gras
    print('\033[94m\033[1m' + texte + '\033[0m')
def vert_gras(texte): # Permet d'imprimer une chaine de caractère en bleu et en gras
    print('\033[92m\033[1m' + texte + '\033[0m')
    
def imprimante():  
    print(tableau_final)
    print()
    print()
    print()
    bleu_gras("Bienvenue")
    print()
    rouge("----------------------------")
    print()
    bleu_gras("Voici la liste de tous les évènements qui auront lieu pendant votre séjour")
    print()
    for sous_tab in base_de_donnee:
        for sous_sous_tab in sous_tab:
            print(sous_sous_tab)
            print()
    print()
    rouge("--------------------------------------------------------------------------------------")
    print()
    bleu_gras("Et voici tous les sports auxquels vous pourriez assisiter")
    print()
    rouge("--------------------------------------------------------------------------------------")
    print()
    for sous_tab in tableau_final:
        for sous_sous_tab in sous_tab:
            print(sous_sous_tab)
            print()
    print()
    vert_gras("Merci d'avoir fait appel à nous !")
    print()
    print()

"""imprimante()"""
                        
            
#############################################
# Fonctions utiles de présentation visuelle #
#############################################

#Couleurs du texte : Vous pouvez utiliser des séquences d'échappement ANSI pour changer la couleur du texte. Voici quelques exemples :

#print('\033[91m' + 'Texte en rouge' + '\033[0m')  # Rouge
#print('\033[92m' + 'Texte en vert' + '\033[0m')  # Vert
#print('\033[94m' + 'Texte en bleu' + '\033[0m')  # Bleu

#Effets visuels : Vous pouvez également ajouter des effets visuels tels que le gras, l'italique et le soulignement en utilisant les séquences d'échappement ANSI. Voici quelques exemples :

#print('\033[1m' + 'Texte en gras' + '\033[0m')          # Gras
#print('\033[3m' + 'Texte en italique' + '\033[0m')      # Italique
#print('\033[4m' + 'Texte souligné' + '\033[0m')         # Souligné
#print('\033[1m\033[3m' + 'Texte en gras et italique' + '\033[0m')  # Gras et italique

#Alignement à droite : Par défaut, la fonction print() aligne le texte à gauche. Cependant, vous pouvez utiliser la méthode str.rjust() pour aligner le texte à droite. Par exemple :

#texte = 'Exemple'
#print(texte.rjust(20))  # Alignement à droite avec un espace de 20 caractères


#######################
# Fonctions obsolètes #
#######################



