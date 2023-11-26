######################################
# Regroupement sports par catégories #
######################################

Aquatiques = ("Canoë","canoë","Pentathlon","pentathlon","Natation","natation","Natation artistique","natation artistique","Natation marathon","natation marathon","Plongeon","plongeon","Waterpolo","waterpolo","Voile","voile","Surf","surf","aviron","Aviron")
Raquette = ("Badminton","badminton","Tennis","tennis","Tennis de table","tennis de table")
Endurance = ("Athlétisme","athlétisme","cyclisme","Cyclisme","Pentathlon","pentathlon","natation","Natation","Poney","poney","triathlon","Triathlon")
Équipe = ("Athlétisme","athlétisme","Aviron","aviron","badminton","Badminton","basketball","basketball","Canoë","canoë","Cyclisme","cyclisme","Football","football","Gymnastique","gymnastique","Handball","handball","Hockey","hockey","Pentathlon","pentathlon","Rugby","rugby","Waterpolo","waterpolo","Tennis","tennis","Tennis de Table","poney","Poney","Voile","voile","Volleyball","volleyball","Volleyball de plage","volleybal de plage")
Individuel = ("Athlétisme","athlétisme","Boxe","boxe","Canoë","canoë","Cyclisme","Cyclisme","BMX","VTT","Escrime","escrime","Golf","golf","Gymnastique","gymnastique","Trampoline","trampoline","Halthérophilie","haltérophilie","Judo","judo","Lutte","lutte","Natation","natation","Pentathlon","pentathlon","Taekwondo","taekwondo","Tennis","tennis","Tennis de table","tennis de table","Tir","tir","tir à l'arc","Tir à l'arc","Triathlon","triathlon","Breaking","breaking","Escalade","escalade","Skateboard","skateboard","Surf","surf")
Balle = ("Basketball","basketball","Football","football","Golf","golf","Handball","handball","Hockey","hockey","Rugby","rugby","Waterpolo","waterpolo","Tennis","tennis","Volleyball","Volleyball de plage","volleyball","volleyball de plage")


####################################################
# Base de donnée pour les sports préférés par pays #
####################################################

class points:

    def __init__(self, nom, pays_prefs, best): 
        self.nom = nom
        self.pays_prefs = pays_prefs
        self.best = best
    

athletisme = points( "athletisme" , ["Antilles néerlandaises","Algérie","Bahamas","Belgique","Bahrein","Iles Caimans","Cameroun","Costa Rica","Cuba","République dominicaine","Equateur","Erythrée","Estonie","Ethiopie","Finlande","France","Royaume-Uni","Grèce","Jamaique","Kenya","Lettonie","Maroc","Nigéria","Nouvelle-Zélande","Panama","Pologne","Portugal","Qatar","Afrique du Sud","Russie","Somalie","Suède","Tanzanie","Trinité-et-Tobago","Tunisie","Ukraine"], ["Etats-Unis","Kenya","Jamaique","Ethiopie","Royaume-Uni"])
aviron= points("aviron",["Canada","Danemark","Royaume-Uni","Pologne"],["Pays-Bas","Royaume-Uni","Italie","Etat-Unis","Roumanie"])
badminton= points( "badminton" ,["Chine","Indonésie","Malaisie","Singapour","Thailande"],["Chine","Corée du Sud","Japon","Danemark","Indonésie"])
basketball= points("basketball", ["Angola","Argentine","Bahamas","Bosnie-Herzégovine","Chine","Corée du Sud","Croatie","Espagne","Estonie","France","Grèce","Israel","Italie","Liban","Lituanie","Philippines","Russie","Serbie","Singapour","Slovénie","Soudan du Sud","Tunisie","Etats-Unis"],["Allemagne","Serbie","Etats-Unis","Canada","Lituanie"])
boxe= points("boxe", ["Azerbaidjan","Costa Rica","Iralnde","Moldavie","Mexique","Maurice","Philippines","Corée du Nord","Ukraine"],["Ouzbékistan","Kazakhstan","Russie","Cuba","Inde"])
canoe_kayak= points("canoe_kayak", ["Hongrie","Slovaquie"],["Allemagne","Hongrie","Espagne","Pologne","Canada","Royaume-Uni","France","République Tchèque","Slovénie","Australie"])
bmx = points("bmx", [] , ["France","Royaume-Uni","Chine","Etats-Unis","Australie"])
cyclisme_sur_piste= points("cyclisme_sur_piste" , ["Royaume-Uni","Malaisie","Pays-Bas","Nouvelle-Zélande"],["Royaume-Uni","Allemagne","Pays-Bas","Australie","Nouvelle Zélande"])
cyclisme_sur_route= points( "cyclimse_sur_route", ["Andorre","Australie","Autriche","Belgique","Burkina Faso","Colombie","Cuba","République tchèque","Danemark","Espagne","Estonie","France","Gabon","Allemagne","Irlande","Italie","Kazakhstan","Luxembourg","Pays-Bas","Qatar","Afrique du Sud","Russie","Slovénie","Suisse","Suède","Ukraine","Vénézuela"],["Pays-Bas","Belgique","Royaume-Uni","Danemark","Etats-Unis"])
escalade= points("escalade" , ["Suisse"],["Japon","Etats-Unis","France","Autriche","Slovénie"])
escrime= points ("escrime" ,["France","Hongrie","Italie","Roumanie"],["Italie","France","Hongrie","Japon","Etats-Unis"])
football = points("football" , ["Afghanistan","Afrique du Sud", "Albanie","Algérie","Allemagne", "Andorre", "Angola", "Antilles néerlandaises", "Arabie saoudite", "Argentine", "Arménie","Aruba", "Autriche", "Azerbaïdjan", "Bahreïn","Bangladesh", "Biélorussie", "Belgique", "Belize", "Bénin", "Bolivie", "Bosnie-Herzégovine", "Botswana", "Brésil", "Brunei", "Bulgarie", "Burkina Faso", "Burundi", "Cambodge", "Cameroun", "Cap-Vert", "Chili", "Colombie", "Comores", "Congo", "Corée du Nord", "Costa Rica", "Côte d’Ivoire", "Chypre", "Croatie", "Danemark", "Djibouti", "Équateur", "Égypte", "El Salvador", "Érythrée", "Guinée équatoriale", "Éthiopie", "France", "Guyane française", "Gabon", "Gambie", "Géorgie", "Ghana", "Grèce", "Grenade", "Guatemala", "Guinée", "Guinée-Bissau", "Haïti", "Honduras", "Hongrie", "Indonésie", "Îles Salomon", "Iran", "Iraq", "Islande", "Israël", "Italie", "Jordanie", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Koweït", "Kirghizstan", "Laos", "Liban", "Lesotho", "Liberia", "Libye", "Liechtenstein", "Luxembourg", "Madagascar", "Malaisie", "Malawi", "Maldives", "Mali", "Malte", "Mauritanie", "Maurice", "Mexique", "Micronésie", "Moldavie", "Monaco", "Maroc", "Monténégro", "Mozambique", "Myanmar", "Namibie", "Niger", "Nigeria", "Macédoine du Nord", "Norvège", "Oman", "Ouganda", "Ouzbékistan", "Palestine", "Paraguay", "Pays-Bas", "Pérou", "Pologne"," Portugal", "Qatar", "République centrafricaine", "République démocratique du Congo", "Roumanie", "Royaume-Uni", "Russie", "Rwanda", "Saint-Kitts-et-Nevis", "Sainte-Lucie", "Saint-Marin", "São Tomé-et-Principe", "Sénégal", "Serbie", "Seychelles", "Sierra Leone", "Singapour", "Slovaquie", "Slovénie", "Somalie", "Soudan", "Soudan", "Suriname", "Suède", "Suisse", "Syrie", "Tadjikistan", "Tchad", "Tanzanie", "Thaïlande", "Timor-Leste", "Togo", "Tunisie", "Turquie", "Turkménistan", "Tuvalu", "Ukraine", "Uruguay", "Vanuatu", "Vietnam", "Yémen", "Zambie","Zimbabwe"],["Espagne","Argentine","France","Royaume-Uni","Suède"])
golf= points("golf" , ["Irlande","Japon","Corée du Sud","Afrique du Sud","Etats-Unis"],["Etats-Unis","Royaume-Uni","Corée du Sud","Espagne","Australie"])
gymnastique= points("gymnastique" , ["Chine","Roumanie"],["Etats-Unis","Japon","Chine","Royaume-Uni","Brésil","Israel","Italie","Allemagne","Bulagrie","Espagne"])
haltérophilie= points( "haltérophilie", ["Bulgarie","Iles Caimans","Iran","Nauru","Tunisie"],["Chine","Colombie","Corée du Sud","Arménie","Thailande"])
handball= points("handball",["Algérie","Croatie","Danemark","Espagne","France","Allemagne","Islande","Roumanie","Russie","Serbie","Slovénie","Suisse","Suède","Handball"],["Danemark","France","Espagne","Suède","Allemagne"])
hockey_sur_gazon = points("hockey_sur_gazon",["Bangladesh","Inde","Pays-Bas","Pakistan","Autorité palestinienne"], [])
judo = points("judo",["Algérie","Egypte","France","Georgie","Japon","Mongolie","Corée du Nord","Ouzbékistan"],["Japon","France","Géorgie","Italie","Ouzbékistan"])
karaté= points("karaté",["Japon"],["Japon","Egypte","Italie","Espagne","France"])
lutte= points("lutte",["Azerbaijan","Bulgarie","Georgie","Iran","Kenya","Kirghizistan","Mongolie","Tadjikistan","Turkménistan","Tunisie","Ouzbékistan"],["Etats-Unis","Japon","Iran","Turquie","Géorgie"])
natation= points("natation", ["Australie","France","Mexique","Monaco","Pays-Bas","Zimbabwe"],["Etats-Unis","Australie","Chine","Royaume-Uni","Canada"])
natation_synchronisee= points("natation_synchronisee",["Russie"],["Japon","Espagne","Chine","Autriche","Royaume-Uni"])
pentathlon = points("pentathlon" , [] , ["Egypte","Italie","Royaume-Uni","Mexique","Corée du Sud"])
plongeon= points("plongeon",["Chine"],["Chine","Mexique","Australie","Royaume-Uni","Canada"])
rugby_a_7= points("rugby_a_7",["Autralie","Fidji","Royaume-Uni","Nouvelle-Zélande","Papouasie-Nouvelle-Guinée","Russie","Tonga"], [])
skateboard = points("skateboard" , [] , ["Japon","Brésil","Etats-Unis","Australie","Royaume-Uni"])
sports_equestres= points("sports_equestres",["France","Royaume-Uni","Irlande","Japon","Mongolie","Emirats arabes unis","Etats-Unis"],["Royaume-Uni","Allemagne","Suède","Pays-Bas","Danemark"])
surf = points("surf", [] , ["Brésil","Australie","Etats-Unis","France","Japon"])
taekwondo= points("taekwondo",["Afghanistan","Corée du Sud","Corée du Nord"],["Croatie","Turquie","Corée du Sud","Ouzbékistan","Royaume-Uni"])
tennis= points("tennis", ["Australie","Belgique","Chili","Chypre","Espagne","France","Monaco","Russie","Serbie","Suisse","Suède","Etats-Unis"],["Etats-Unis","Serbie","République Tchèque","Espagne","Pologne"])
tennis_de_table= points("tennis_de_table",["Cambodge","Chine","Corée du Sud","Singapour"],["Chine","Japon","Corée du Sud","Allemagne","Suède"])
tir= points("tir",["Etats-Unis"],["Chine","Etats-Unis","Corée du Sud","Inde","Ukraine"])
tir_a_arc= points("tir_a_arc",["Bhoutan","Corée du Sud","Mongolie"],["Inde","Corée du Sud","Pays-Bas","Mexique","Turquie"])
trampoline = points("trampoline", [] , ["Royaume-Uni","Etats-Unis","Australie","France","Portugal"])
triathlon = points("triathlon", [] , ["France","Royaume-Uni","Nouvelle Zélande","Portugal","Etats-Unis"])
voile = points("voile",["Anguilla","Espagne","Royaume-Uni","Italie","Nouvelle-Zélande"],["Royaume-Uni","Pays-Bas","Italie","Israel","France"])
volleyball= points("volleyball",["Cambodge","Italie","Pologne","Sri Lanka"],["Pologne","Etats-Unis","Turquie","Japon","Italie"])
volleyball_de_plage= points("volleyball_de_plage",["Brésil"],["Brésil","Canada","Norvège","Etats-Unis","Allemagne"])
vtt = points("vtt", [] , ["France","Royaume-Uni","Suisse","Autriche","Nouvelle Zélande"])
water_polo= points("water_polo",["Hongrie","Serbie"] , [])

Sports=[athletisme,aviron,badminton,basketball,boxe,canoe_kayak,cyclisme_sur_piste,cyclisme_sur_route,escalade,escrime,football,golf,gymnastique,handball,hockey_sur_gazon,haltérophilie,judo,karaté,lutte,natation,natation_synchronisee,plongeon,sports_equestres,taekwondo,tennis,tennis_de_table,tir,tir_a_arc,voile,volleyball,volleyball_de_plage,water_polo]

sports={"athlétisme":athletisme.pays_prefs, "aviron":aviron.pays_prefs,"badminton":badminton.pays_prefs,"basketball":basketball.pays_prefs,"boxe":boxe.pays_prefs,"canoe-kayak":canoe_kayak.pays_prefs,"cyclisme sur piste":cyclisme_sur_piste.pays_prefs,"cyclisme sur route":cyclisme_sur_route.pays_prefs,"escalade":escalade.pays_prefs,"escrime":escrime.pays_prefs,"football":football.pays_prefs,"golf":golf.pays_prefs,"gymnastique":gymnastique.pays_prefs,"handball":handball.pays_prefs,"hockey sur gazon":hockey_sur_gazon.pays_prefs,"hatérophilie":haltérophilie.pays_prefs,"judo":judo.pays_prefs,"karaté":karaté.pays_prefs,"lutte":lutte.pays_prefs,"natation":natation.pays_prefs,"natation synchronysée":natation_synchronisee.pays_prefs,"plongeon":plongeon.pays_prefs,"sports équestres":sports_equestres.pays_prefs,"taekwondo":taekwondo.pays_prefs,"tennis":tennis.pays_prefs,"tennis de table":tennis_de_table.pays_prefs,"tir":tir.pays_prefs,"tir à l'arc":tir_a_arc.pays_prefs,"voile":voile.pays_prefs,"volleyball":volleyball.pays_prefs,"volleyball de plage":volleyball_de_plage.pays_prefs,"water polo":water_polo.pays_prefs}

best_sports={"athlétisme":athletisme.best,"aviron":aviron.best,"badminton":badminton.best,"basketball":basketball.best,"BMX":bmx.best,"boxe":boxe.best,"canoe-kayak slalom":canoe_kayak.best,"canoe-kayak sprint":canoe_kayak.best,"cyclisme de route":cyclisme_sur_route.best,"cyclisme sur piste":cyclisme_sur_piste.best,"VTT":vtt.best,"escalade":escalade.best,"escrime":escrime.best,"football":football.best,"golf":golf.best,"gymnastique":gymnastique.best,"gymnastique rythmique":gymnastique.best,"haltérophilie":haltérophilie.best,"handball":handball.best,"judo":judo.best,"karaté":karaté.best,"lutte":lutte.best,"natation":natation.best,"natation synchronisée":natation.best,"pentathlon moderne":pentathlon.best,"plongeon":plongeon.best,"skateboard":skateboard.best,"sports équestres":sports_equestres.best,"surf":surf.best,"taekwondo":taekwondo.best,"tennis":tennis.best,"tennis de table":tennis_de_table.best,"tir":tir.best,"trampoline":trampoline.best,"triathlon":triathlon.best,"voile":voile.best,"volleyball":volleyball.best,"volley de plage":volleyball_de_plage.best}