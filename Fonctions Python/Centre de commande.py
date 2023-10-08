##############
# Librairies #
##############

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import copy

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

##################################################
# Nouvelles fonctions en rapport avec les points #
##################################################




#########################################
# Fonctions de tranformation de l'heure #
#########################################

# Fonction permettant d'associer une valeur exploitable à notre date (Non utilisée finalement)

def transformation_date(tableau_entree):
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



################################
# Poste de contrôle du contenu #
################################
print()
print()


base_de_donnee = 1

tableau_final = 1






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

imprimante()
                        
            
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



