#TIPE
print()
#Fonction qui lit dans un fichier texte les informations données par l'utilisateur et qui renvoit les matchs qui correspondent à ses demandes

##############
# Librairies #
##############
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt

##############
# Variables #
##############

#tableaux qui vont venir stocker les données de l'utilisateur

data=[[],[],[],[],[]]   #data[0][] = date data[1][] = genre data[2][] = sports data[3][] = sous sports  data[4][] = nations

#########################
# Lire le fichier texte #
#########################

# Fonction qui lit les éléments du fichier texte rennvoyé par l'utilisateur et qui extrait les données

def lire_donnee(fichier):
    with open(fichier, "r", encoding="utf8") as f:
        for ligne in f:
            if "Date:" in ligne:
                mots = ligne.split()
                x= len(mots) -1
                while (x != 0):
                    data[0].append(mots[x])
                    x-=1
            elif "Genre:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    data[1].append( mots[x])
                    x-=1
            elif "Sports:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    data[2].append(mots[x])
                    x-=1
            elif "Sous_sports:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    data[3].append(mots[x])
                    x-=1
            elif "Nation:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    data[4].append(mots[x])
                    x-=1
    return data

########################################
# Fonction de tranformation de l'heure #
########################################

def transformation_date_2(data): 
    format_date = "%d/%m/%y"
    date = dt.strptime(data, format_date).date()
    return date

########################################
# Fonction auxiliaire gestion de ligne #
########################################

# Cette fonction va permettre de récupérer uniquement certaines lignes de notre base de donnée, fonctionnalité non native à la fonction loadtxt

def generate_specific_rows(filePath, userows=[]):
    with open(filePath) as f:
        for i, line in enumerate(f):
            if i in userows:
                yield line
                
#############################################
# Fonction auxiliaire tranformation tableau #
#############################################

# Cette fonction va permettre de transformer l'écriture d'un tableau afin que l'exploitation de ses données soit plus facile par la suite 

def transposee(tab):
    tab_rep = np.transpose(tab)
    return tab_rep
            
        


########################################
# Chercher les données correspondantes #
########################################

def chercher_donnee (data):

    # Variables qui seront utilisées dans cette fonction
    
    match=[]
    tab_indices = []
    data=lire_donnee(r"/Users/lg/Documents/Prépa /TIPE /information_utilisateur.csv")   #fichier texte avec les informations de l'utilisateur
    date_arrivee = transformation_date_2(data[0][1])
    date_retour = transformation_date_2(data[0][0])
    
    # On balaye tous les fichiers afin de trouver le bon
    
    for i in range (len(data[1])):
        for j in range(len(data[2])):
            for k in range(len(data[3])):
                
                # On charge la base de données correspondante
                dates_rencontres = np.loadtxt(r"/Users/lg/Documents/Prépa /TIPE /Base de données TIPE/"+data[1][i]+"/"+data[2][j]+"/"+data[3][k]+"/TIPE_"+data[1][i]+"_"+data[2][j]+"_"+data[3][k]+".csv", dtype= str, delimiter=";", skiprows=11, usecols=1, ndmin = 1, encoding="utf8")   #va chercher dans le bon fichier
                # Ce tableau contient toutes les dates auxquels il y a des matchs pour le sport sélectionné
                
                for l in range (len(dates_rencontres)-1) :
                    if date_arrivee <= transformation_date_2(dates_rencontres[l]) <= date_retour :       # Vérifie si la date de la recontre est incluse dans la période de visite de l'utilisateur
                        tab_indices.append(l+11)
                
                # Désormais nous avons les indices de tous les matchs auxquel notre utilisateur peut assister    
                       
                gen = generate_specific_rows(r"/Users/lg/Documents/Prépa /TIPE /Base de données TIPE/"+data[1][i]+"/"+data[2][j]+"/"+data[3][k]+"/TIPE_"+data[1][i]+"_"+data[2][j]+"_"+data[3][k]+".csv", userows=tab_indices)
                infos_matchs= np.loadtxt(gen, dtype = str, delimiter=";", usecols=(0,1,2,3,4), ndmin = 2, unpack='true', encoding="utf8")   #va chercher dans le bon fichier     
                
                # Grâce aux indices, nous avons pu récupérer toutes les données des maths qui pourront être séléctionnés

                # On transpose la matrice de nos match
                
                
                
                
    return transposee(infos_matchs)


print("Ici est affiché l'ensemble des matchs auxquels nous pouvons assister")
print()
print(chercher_donnee(data))
print()
print("--------------------------------------------------------------------")
print()

################################
# Mise en commun des fonctions #
################################

from datetime import datetime


# Ce fichier contient une fonction qui, sur base de l'entrée de différente plage horaire va retourner les sessions auxquelles l'utilisateur va pouvoir participer, sur base de la première valide #

tableau_entree = chercher_donnee(data) 


# Fonction permettant d'associer une valeur exploitable à notre date

def transformation_date(tableau_entree):
    for i in range(len(tableau_entree)):
        date = tableau_entree[i][1]
        format_date = "%d/%m/%y"
        tableau_entree[i][1] = datetime.strptime(date, format_date).date()
    return tableau_entree


# Fonction permettant d'associer une valeur exploitable à nos heures de début et fin

def transformation_heure(tableau_entree):
    for i in range(len(tableau_entree)):
        heure_debut = tableau_entree[i][2]
        format_heure = "%H:%M"
        tableau_entree[i][2] = datetime.strptime(heure_debut, format_heure).time()
        heure_fin = tableau_entree[i][3]
        tableau_entree[i][3] = datetime.strptime(heure_fin, format_heure).time()
    return tableau_entree


# Dictionnaire pour le tri du tableau 
    
def cle_tri(element):
    sport = element[0]
    #ss_sport = element[1]
    date = element[1]
    heure_debut = element[2]
    return (sport, date, heure_debut)

# Fonction qui utilise ce dictionnaire pour trier notre tableau

def tri_croissant(tableau):
    tableau = sorted(tableau, key=cle_tri)
    return tableau
    
# Fonction qui permet de supprimer toutes les superpositions d'horaires
    
def ejection(tableau):
    i = 0
    while i < len(tableau)-1:
        if tableau[i][1] == tableau[i+1][1] :
            if (tableau[i][3]) > tableau[i+1][2]:
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

print("Ici est affiché l'ensemble des matchs auxquels nous pouvons réellement assiter")
print()
for sous_tableau in tableau_final:
    print(sous_tableau)
    print()