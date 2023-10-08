

######################################
# Regroupement sports par catégories #
######################################

Aquatiques = ("Canoë","canoë","Pentathlon","pentathlon","Natation","natation","Natation artistique","natation artistique","Natation marathon","natation marathon","Plongeon","plongeon","Waterpolo","waterpolo","Voile","voile","Surf","surf","aviron","Aviron")
Raquette = ("Badminton","badminton","Tennis","tennis","Tennis de table","tennis de table")
Endurance = ("Athlétisme","athlétisme","cyclisme","Cyclisme","Pentathlon","pentathlon","natation","Natation","Poney","poney","triathlon","Triathlon")
Équipe = ("Athlétisme","athlétisme","Aviron","aviron","badminton","Badminton","basketball","basketball","Canoë","canoë","Cyclisme","cyclisme","Football","football","Gymnastique","gymnastique","Handball","handball","Hockey","hockey","Pentathlon","pentathlon","Rugby","rugby","Waterpolo","waterpolo","Tennis","tennis","Tennis de Table","poney","Poney","Voile","voile","Volleyball","volleyball","Volleyball de plage","volleybal de plage")
Individuel = ("Athlétisme","athlétisme","Boxe","boxe","Canoë","canoë","Cyclisme","Cyclisme","BMX","VTT","Escrime","escrime","Golf","golf","Gymnastique","gymnastique","Trampoline","trampoline","Halthérophilie","haltérophilie","Judo","judo","Lutte","lutte","Natation","natation","Pentathlon","pentathlon","Taekwondo","taekwondo","Tennis","tennis","Tennis de table","tennis de table","Tir","tir","tir à l'arc","Tir à l'arc","Triathlon","triathlon","Breaking","breaking","Escalade","escalade","Skateboard","skateboard","Surf","surf")
Balle = ("Basketball","basketball","Football","football","Golf","golf","Handball","handball","Hockey","hockey","Rugby","rugby","Waterpolo","waterpolo","Tennis","tennis","Volleyball","Volleyball de plage","volleyball","volleyball de plage")




#######################################################
# Fonctions de vérification d'appartenance des sports #
#######################################################








####################################
# Fonction d'attribution de points #
####################################

def attribuer_points(tab,x):
    y=tab[2][0]
    tab[2]=x+y
    return tab


t=[[["volley"],["finale"],[6]],[["hand"],["quart de finale"],[1]],[["basket"],["huitieme"],[5]]]


attribuer_points(t[0],2)
print(t)
