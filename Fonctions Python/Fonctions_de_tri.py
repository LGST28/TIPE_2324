##############
# Librairies #
##############
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
from datetime import datetime # À corriger
import copy

######################################
# Fonction globale de tri des sports #
######################################

# Cette fonction permet de supprimer les overlaps au sein d'un même sport, c'est une sécrutié en cas de problème dans la base de données

def ejection_locale(tableau):
    tab = tableau.copy()
    i = 0
    while i < len(tab) - 1:
        if (tab[i][1] == tab[i+1][1]) and (tab[i][3] > tab[i+1][2]):
            del tab[i+1]
        i += 1
    return tab

# Cette fonction permet de supprimer toutes les séances auxquels nous ne pouvons pas assister, en prenant le premier sport comme argument principal (Fonctionne pour deux sports)

def ejection_globale(tableau):
    tab_inter = tableau.copy()
    for i in range(len(tab_inter)):
        tab_inter[i] = ejection_locale(tab_inter[i])
    # Désormais les sous-tableaux propres à chacun des sports sont triés 
    i = 0 
    while i < len(tab_inter) - 1:
        j = i
        while j < len(tab_inter[i]):
            k = 0
            while k < len(tab_inter[i+1]):             
                if tab_inter[i][j][1] == tab_inter[i+1][k][1] and (tab_inter[i][j][3] > tab_inter[i+1][k][2] and tab_inter[i][j][2] <= tab_inter[i+1][k][2]):
                    #Les deux conditions à vérifier sont : 1. Le début de l'épreuve 2 ne doit pas être avant la fin de l'épreuve 1; et tout cela sachant que l'épreuve deux ne commence pas avant l'épreuve 1
                    del tab_inter[i+1][k]
                else: 
                    k += 1
            j += 1
        i += 1
    
    return tab_inter

# Cette fonction permet de supprimer toutes les séances auxquels nous ne pouvons pas assister, en prenant le premier sport comme argument principal (Fonctionne pour n sports)
    
def ejection_globale_n(tableau):
    tab = copy.deepcopy(tableau) # Permet de copier le tableau en totalité, avec ses sous_tableaux et évite de modifier le tableau en entrée et ainsi la base de données
    for i in range(len(tab)):
        sous_tab_1 = tab[i]
        for j in range(len(sous_tab_1)-1):
            sport_1 = sous_tab_1[j]
            for k in range(i, len(tab)):
                sous_tab_2 = tab[k]
                start_index = j + 1 if k == i else 0  # Ignorer les éléments précédents dans le même sous-tableau
                for l in range(start_index, len(sous_tab_2)):
                    sport_2 = sous_tab_2[l]
                    # Comparer les éléments element1 et element2
                    #print("Comparaison :", sport_1, "et", sport_2)
                    # Désormais nous pouvons comparer chacun des sports entre eux et supprimer ceux ne nous intéressant pas 
                    if (sport_1[1] == sport_2[1]) and (sport_1[3] > sport_2[2] and sport_1[2] <= sport_2[2]):
                        # Print de débeugage si nécessaire
                        """print()
                        print("Actuellement je compare :", sport_1, "et", sport_2)
                        print("Je supprime alors :", sport_2)
                        print("-----------------")"""
                        sous_tab_2.pop(l)  # Supprimer sport_2 de sous_tab_2, on doit utiliser pop car 'sport_2' est une référence locale et n'affecte pas le tableau
                        break  # Sortir de la boucle l après la suppression
    
    return tab



######################################
# Tri par ordre croissant de points #
######################################

# Cette fonction permet de tirer les rencontres en fonction du nombre de points qu'elles ont

def tri_tableau(t,indice):
    n =len(t)
    for i in range (1,n):
        k=t[i][indice]
        #print(k)#
        j= i-1
        while j>=0 and t[j][indice]<k:
            tmp=t[j]
            t[j]=t[j+1]
            t[j+1]=tmp
            j=j-1
    print(t)


"""t=[[["volley"],[3]],[["hand"],[1]],[["basket"],[5]]]"""

#tri_tableau(t,1)