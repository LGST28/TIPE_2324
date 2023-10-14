##############
# Librairies #
##############

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import copy
from Fonctions_de_création import creation_donnees, lire_donnee
#from Fonctions_attributions_points import 
from Fonctions_utiles import add_info
from Base_de_données import *

##################################
# Import de fonctions provisoire #
##################################

def n_p_ajout_point_globale(liste, n):
    l_rep = liste
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            l_rep[i][j][indice_points] = n
    return l_rep


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

dates_utilisateur = lire_donnee(r"/Users/lg/Library/CloudStorage/OneDrive-Personnel/Prépa/Spé/TIPE/TIPE_2324/information_utilisateur_double.csv")[0]
# Faire attention, pour l'instant les dates sont inversées, avec le retour en premier (indice 0)
 

################################
# Poste de contrôle du contenu #
################################



base_de_donnee = 1

tableau_final = 1

def n_p_ajout_point_globale(liste, n):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            liste[i][j][indice_points] = n
    return liste
                
##############################################
# Poste de commande de l'appel des fonctions #
##############################################

# On créé notre tableau avec tous les sports auxquels l'utilisateur peut assister 

l_sports = creation_donnees()
print()
print()
print(l_sports)
print()
print()
l_sports_av_points = add_info(l_sports)
print(l_sports_av_points)
print()
print()

# Désormais nous avons tous nos points présents et égaux à 0.  

#print(l_sport_av_points)

l_sports_av_points_0 = n_p_ajout_point_globale(l_sports_av_points,0)
print(l_sports_av_points_0)
print()
print()

# On créé un tableau qui va contenir chacune de nos simulations
# Les simulations 1 représentent l'application des fonctions date -> points -> dates

simu_tab_1 = []

# Les simulations 2 représentent l'application des fonctions points -> dates

# On fait des boucles qui font varier les paramètres des points, et pour chaque boucle on va récupérer le tableau de sortie, et donc le tableau proposé
'''
for i in range (1,5):
    for j in range (3,8):
        for k in range (1,5):
            for l in range (1,5):
                points_nationalité = i
                points_finale = j
                points_demi = j - 1
                points_quart = j - 3 



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



