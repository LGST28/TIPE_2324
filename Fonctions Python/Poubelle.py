######################################
# Premières recherches d'algorithmes #
######################################

"""def ejection_globale(tableau):
    i = 0
    while i < len(tableau):
        j = 0
        while j < len(tableau[i]):
            k = 0
            while (j + k) < len(tableau[i]) - 1 and (i+k) < len(tableau[i+1]):
                if ((tableau[i][j][1] == tableau[i][j+k][1]) and (tableau[i][j][1] == tableau[i+k][j+k-i][1])) or ((tableau[i][j][3] < tableau[i][j+k][2]) or (tableau[i][j][3] < tableau[i+k][j+k][2])):
                    print("Zbeub")
                    del tableau[i+1][i+k+j-1]
                    
                k += 1
                    
                    
                if (tableau[i][j][1] == tableau[i][j+k][1]) and (tableau[i][j][3] > tableau[i][j+k][2] or tableau[i][j][2] < tableau[i][j+k][3]):
                    del tableau[i+1][j+k]
                    print("Bob")
                elif tableau[i][j][1] == tableau[i+k][j][1] and (tableau[i][j][3] > tableau[i+k][j][2] or tableau[i][j][2] < tableau[i+k][j][3]):
                    del tableau[i+k][j]
                    print("Patrick")
            j += 1
        i += 1

    return tableau"""


"""def ejection_locale(tableau):
    tab = tableau.copy()
    i = 0
    while i < len(tab) - 1:
        if (tab[i][1] == tab[i+1][1]) and (tab[i][3] > tab[i+1][2]):
            del tab[i+1]
        i += 1
    return tab

def ejection_globale(tableau):
    tab_inter = tableau.copy()
    for i in range(len(tab_inter)):
        tab_inter[i] = ejection_locale(tab_inter[i])
    # Désormais les sous-tableaux propres à chacun des sports sont triés 
    

    i = 0 
    while i < len(tab_inter) :
            j = 0
            while j < len(tab_inter[i]):
                k = j
                while j + k < len(tab_inter[i+1]):
                    if tab_inter[i][j][1] == tab_inter[i+1][k][1] and (tab_inter[i][j][3] > tab_inter[i+1][k][2] and tab_inter[i][j][2] <= tab_inter[i+1][k][2]):
                        Les deux conditions à vérifier sont : 1. Le début de l'épreuve 2 ne doit pas être avant la fin de l'épreuve 1; et tout cela sachant que l'épreuve deux ne commence pas avant l'épreuve 1
                        print(tab_inter[i+1][k])
                        print()
                        print("i =", i)
                        print("j = ", j)
                        print("k = ",k)
                        del tab_inter[i+1][k]
                        print()
                        print("Coucou ma belle")
                        print()
                    
                    else: 
                        k += 1
                j += 1
            i += 1
    
    return tab_inter"""
    
    
"""def ejection_globale_n(tableau):
    tab_inter = tableau.copy()
    for i in range(len(tab_inter)):
        tab_inter[i] = ejection_locale(tab_inter[i])
    # Désormais les sous-tableaux propres à chacun des sports sont triés 
    i = 0 
    while i < len(tab_inter) - 1:
        m = 1
        print("Ici nous avons i : ", i)
        j = 0
        print("Ici nous avons j : ", j)
        while j < len(tab_inter[i]) and (i+m<len(tab_inter)):
            print("Ici nous avons m : ", m)
            k = 0  # Réinitialisation de k à zéro
            print("Ici nous avons k : ", k)
            while (k < len(tab_inter[i+m])):
                print("Je suis entré") 
                print("Maintenant k vaut : ", k)  
                print("--------------")
                print("Je considère actuellement :", tab_inter[i][j])      
                print("Que je compare avec :", tab_inter[i+m][k])
                if tab_inter[i][j][1] == tab_inter[i+m][k][1] and (tab_inter[i][j][3] > tab_inter[i+m][k][2] and tab_inter[i][j][2] <= tab_inter[i+m][k][2]) and (i+m != 0):
                    # Les deux conditions à vérifier sont : 1. Le début de l'épreuve 2 ne doit pas être avant la fin de l'épreuve 1; et tout cela sachant que l'épreuve deux ne commence pas avant l'épreuve 1
                    print("Je compare désormais :", tab_inter[i][j])
                    print("Avec : ", tab_inter[i+m][k] )
                    print("Je vais supprimer : ", tab_inter[i+m][k])
                    del tab_inter[i+m][k]
                else: 
                    k += 1
                m+=1
            j += 1
        i += 1
    
    return tab_inter"""
    
    
"""def ejection_globale_n(tableau):
    tab = tableau.copy()
    for i in range(len(tab)):
        sous_tab_1 = tab[i]
        for j in range(len(sous_tab_1)):
            sport_1 = sous_tab_1[j]
            for k in range(i, len(tab)):
                sous_tab_2 = tab[k]
                start_index = j + 1 if k == i else 0  # Ignorer les éléments précédents dans le même sous-tableau
                for l in range(start_index, len(sous_tab_2)):
                    sport_2 = sous_tab_2[l]
                    # Comparer les éléments element1 et element2
                    #print("Comparaison :", sport_1, "et", sport_2)
                    # Désormais nous pouvons comparer chacun des sports entre eux et supprimer ceux ne nous intéressant pas 
                    if (sport_1[1]==sport_2[1]) and (sport_1[3]>sport_2[2] and sport_1[2] <= sport_2[2]):
                        print()
                        print("Actuellement je compare :", sport_1, "et", sport_2)
                        print("Je supprime alors :", sport_2)
                        print("-----------------")
                        del sport_2                    
    return tab   """


"""def transfo_dim_down(tableau):
    # On commence par récupérer les tailles des tableaux à l'entrée de la fonction
    tab_tailles = []
    for i in range(len(tableau)):
        tab_tailles.append(len(tableau[i]))
    # On peut désormais transformer notre tableau de dimension 3 en dimension 2 
    print(nv_tab)"""


#################################
# Premier essai de dictionnaire #
#################################

# Ancien dictionnaire pour le tri du tableau (Utilisé dans le tri de tableaux simples)

def cle_tri(element):
    sport = element[0][0][0]
    #ss_sport = element[1]
    date = element[0][0][1]
    heure_debut = element[0][0][2]
    return (sport, date, heure_debut)

# Fonction qui utilise ce dictionnaire pour trier notre tableau

def tri_croissant(tab):
    tableau = tab
    for i in range (len(tableau)):
        tableau[i] = sorted(tableau, key=cle_tri)
        return tableau
# Recherches de la fonction ejection