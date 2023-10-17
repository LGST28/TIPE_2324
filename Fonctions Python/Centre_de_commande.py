##############
# Librairies #
##############

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import copy
from Fonctions_de_création import creation_donnees, lire_donnee
from Fonctions_attributions_points import n_p_ajout_point_globale # Cet appel à la fonction cause l'erreur
from Fonctions_utiles import add_info, is_in
from Base_de_données import *
from Fonctions_de_tri import *


dossier_racine = r"/Users/lg/Library/CloudStorage/OneDrive-Personnel/Prépa/Spé/TIPE/TIPE_2324/"

##################################
# Import de fonctions provisoire #
##################################

# Voici ici les fonctions qui sont dans d'autres fichiers mais qu'on ne peux pas appeler
'''
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


print()
print()
print()



def pts_pour_type(t):
    if(t[0]=="Finale"):
        attribuer_points(t,points_finale)
    if(t[0]=='Demi finale'):
        attribuer_points(t,points_demi)
    if(t[0]=='Quart de finale'):
        attribuer_points(t,points_quart)
    return t

def pts_pour_nationalité (nationalité,t):
    sport=sports[t[0][0]]
    if is_in(nationalité,sport) :
        attribuer_points(t,points_nationalité)
    return t

'''

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

################################
# Informations sur les indices #
################################

indice_date_rencontre = 1
indice_points = 5

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
points_nationalité = 5
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

l_sports = creation_donnees()
l_sports_av_points = add_info(l_sports)
l_sports_av_points_0 = n_p_ajout_point_globale(l_sports_av_points,0) # On applique la fonction qui se trouve dans un autre fichier

#for sport in l_sports_av_points_0:
#   print(sport)

print()
print()
print()

tab_points_type_1 = []









######################
# Zone de recherches #
######################








# On commence par attribuer les points en fonction du type de rencontre
'''
def fct_points_type_rencontres(tab):
    rep = []
    for i in range (len(tab)): # Ici nous avons chaque sport et on travaille sur les rencontres
        for j in range (len(tab[i])):
            rep.append(pts_pour_type(tab[i][j]))
    return rep

def fct_points_nationalite(tab):
    rep = []
    for i in range (len(tab)): # Ici nous avons chaque sport et on travaille sur les rencontres
        for j in range (len(tab[i])):
            rep.append(pts_pour_nationalité("France",tab[i][j]))
    return rep


test = fct_points_type_rencontres(l_sports_av_points_0)

print(test)

test_2 = fct_points_nationalite(test)
'''
print()
print()
print()

#print(test_2)


print()
print()
print()

#print(tab_points_type_1)

'''
# Désormais nous avons accès à un tableau sur lequel nous pouvons travailler les points

# On créé un tableau qui va contenir chacune de nos simulations
# Les simulations 1 représentent l'application des fonctions date -> points -> dates

simu_tab_1 = []

# Les simulations 2 représentent l'application des fonctions points -> dates

simu_tab_2 = []

# On fait des boucles qui font varier les paramètres des points, et pour chaque boucle on va récupérer le tableau de sortie, et donc le tableau proposé

def tri_simu_1(liste) :

    rep = ejection_globale_n(liste)
    rep = tri_tableau(rep)
    rep = ejection_globale_n(rep)

    return rep

def tri_simu_2(liste) :

    rep = tri_tableau(liste)
    rep = ejection_globale_n(rep)

    return rep


for i in range (1,5):
    for j in range (3,8):
            for l in range (len(l_sports_av_points_0)):
                points_nationalité = i
                points_finale = j
                points_demi = j - 1
                points_quart = j - 3 

                # On traite le premier cas, càd que l'on trie dans un premier temps les rencontres en fonction des dates, avant de trier les points
                # On commence à attribuer les points pour le type de rencontre

                for a in range (len(l_sports_av_points_0[l])): # Ici nous avons chaque sport et on travaille sur les rencontres
                    tab_points_type_1 = pts_pour_type(l_sports_av_points_0[l][a])'''

'''











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

'''

