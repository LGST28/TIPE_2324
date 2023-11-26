##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
import copy
from Fonctions_utiles import transformation_date_locale, transposee

dossier_racine = r"/Users/lg/Library/CloudStorage/OneDrive-Personnel/Prépa/Spé/TIPE/TIPE_2324/"

################################
# Lecture de la base de donnée #
################################

# Fonction auxiliaire qui permet de lire le fichier extrait du site internet

def lire_donnee(fichier):
    modele = [[],[],[],[],[],]
    with open(fichier, "r", encoding="utf8") as f:
        for ligne in f:
            if "Date:" in ligne:
                mots = ligne.split()
                x= len(mots) -1
                while (x != 0):
                    modele[0].append(mots[x])
                    x-=1
            elif "Genre:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    modele[1].append( mots[x])
                    x-=1
            elif "Sports:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    modele[2].append(mots[x])
                    x-=1
            elif "Sous_sports:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    modele[3].append(mots[x])
                    x-=1
            elif "Nation:" in ligne:
                mots = ligne.split()
                x = len(mots) -1
                while (x != 0):
                    modele[4].append(mots[x])
                    x-=1
    return modele
        
# Fonction qui permet de placer en tableau, les différents sports, ainsi que leurs horaires et le type de ces derniers


#########################################
# Fonction auxiliaire - Gestion tableur #
#########################################

# Cette fonction va permettre de récupérer uniquement certaines lignes de notre base de donnée, fonctionnalité non native à la fonction loadtxt

def generate_specific_rows(filePath, userows=[]):
    with open(filePath) as f:
        for i, line in enumerate(f):
            if i in userows:
                yield line
                


########################################
# Creation de la matrice de rencontres #
########################################

def creation_donnees ():

    # Variables qui seront utilisées dans cette fonction
    
    Global = []
    data=lire_donnee(dossier_racine+r"information_utilisateur_double.csv")   #fichier texte avec les informations de l'utilisateur
    date_arrivee = transformation_date_locale(data[0][1])
    date_retour = transformation_date_locale(data[0][0])
    
    # Si la catégorie sous sport n'est pas prévue pour le sport concerné, alors on remplace par vide et on changera le chemin d'accès (Sécurité à faire)
    
    # On balaye tous les fichiers de la base de données afin de trouver le bon
    
    for i in range (len(data[1])):
        for j in range(len(data[2])):
            if (i==j) : 
                for k in range(len(data[3])):
                    infos_matchs = []
                    dates_rencontres = []
                    tab_indices = []
                    
                    if (i==k):
                        
                        # On charge la base de données correspondante
                        # On doit ajouter une condition en fonction de si le chemin d'accès au fichier comporte une sous catégorie ou non
                        
                        if (data[3][k]=="None" and j == k):
                            dates_rencontres = np.loadtxt(dossier_racine+r"Base de données TIPE/"+data[1][i]+"/"+data[2][j]+"/TIPE_"+data[1][i]+"_"+data[2][j]+".csv", dtype= str, delimiter=";", skiprows=11, usecols=1, ndmin = 1, encoding="utf8")   #va chercher dans le bon fichier
                        else:
                            dates_rencontres = np.loadtxt(dossier_racine+r"Base de données TIPE/"+data[1][i]+"/"+data[2][j]+"/"+data[3][k]+"/TIPE_"+data[1][i]+"_"+data[2][j]+"_"+data[3][k]+".csv", dtype= str, delimiter=";", skiprows=11, usecols=1, ndmin = 1, encoding="utf8")   #va chercher dans le bon fichier    
                        
                        # Ce tableau contient toutes les dates auxquels il y a des matchs pour le sport sélectionné
                        
                        for l in range (len(dates_rencontres)) :
                            if date_arrivee <= transformation_date_locale(dates_rencontres[l]) <= date_retour :       # Vérifie si la date de la recontre est incluse dans la période de visite de l'utilisateur
                                tab_indices.append(l+11)
                        
                        # Désormais nous avons les indices de tous les matchs auxquel notre utilisateur peut assister    
                        # De même nous devons considérer le cas où le sport en question ne prévois pas de sous catéogrie

                        if (data[3][k]=="None" and j==k):
                            gen = generate_specific_rows(dossier_racine+r"Base de données TIPE/"+data[1][i]+"/"+data[2][j]+"/TIPE_"+data[1][i]+"_"+data[2][j]+".csv", userows=tab_indices)
                            infos_matchs.append(transposee(np.loadtxt(gen, dtype = str, delimiter=";", usecols=(0,1,2,3,4,5), ndmin = 2, unpack='true', encoding="utf8")))   #va chercher dans le bon fichier   
                            infos_matchs = np.concatenate(infos_matchs)
                        else :
                            gen = generate_specific_rows(dossier_racine+r"Base de données TIPE/"+data[1][i]+"/"+data[2][j]+"/"+data[3][k]+"/TIPE_"+data[1][i]+"_"+data[2][j]+"_"+data[3][k]+".csv", userows=tab_indices)
                            infos_matchs.append(transposee(np.loadtxt(gen, dtype = str, delimiter=";", usecols=(0,1,2,3,4,5), ndmin = 2, unpack='true', encoding="utf8")))  #va chercher dans le bon fichier 
                            infos_matchs = np.concatenate(infos_matchs)
                         
                        # Grâce aux indices, nous avons pu récupérer toutes les données des maths qui pourront être séléctionnés
                        # Ne pas oublier de transposer la matrice !
                    
                        if len(infos_matchs) > 0:
                            infos_matchs = np.concatenate(infos_matchs)
                            infos_matchs = np.reshape(infos_matchs, (-1, 6))  # Redimensionner le tableau à 2 dimensions (5 colonnes)
                            Global.append(infos_matchs)  # Ajouter infos_matchs à Global sous forme de liste
                        
                        #print("Ceci est info_match")
    
    # Après chaque tout de boucle, nous allons obtenir des tableaux Numpy, cette ligne permet de tout convertir en tableau normal de python                                 
    Final = [sous_global.tolist() for sous_global in Global]
    return Final



###################################
# Attribution des points initiaux #
###################################


# Maintenant que nous avons une ou plusieurs cases en plus, nous allons pouvoir attribuer les points initiaux à chacune de nos rencontres


