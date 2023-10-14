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





####################################################
# Base de donnée pour les sports préférés par pays #
####################################################

athletisme =["Antilles néerlandaises","Algérie","Bahamas","Belgique","Bahrein","Iles Caimans","Cameroun","Costa Rica","Cuba","République dominicaine","Equateur","Erythrée","Estonie","Ethiopie","Finlande","France","Royaume-Uni","Grèce","Jamaique","Kenya","Lettonie","Maroc","Nigéria","Nouvelle-Zélande","Panama","Pologne","Portugal","Qatar","Afrique du Sud","Russie","Somalie","Suède","Tanzanie","Trinité-et-Tobago","Tunisie","Ukraine"]
aviron=["Canada","Danemark","Royaume-Uni","Pologne"]
badminton=["Chine","Indonésie","Malaisie","Singapour","Thailande"]
basketball=["Angola","Argentine","Bahamas","Bosnie-Herzégovine","Chine","Corée du Sud","Croatie","Espagne","Estonie","France","Grèce","Israel","Italie","Liban","Lituanie","Philippines","Russie","Serbie","Singapour","Slovénie","Soudan du Sud","Tunisie","Etats-Unis"]
boxe=["Azerbaidjan","Costa Rica","Iralnde","Moldavie","Mexique","Maurice","Philippines","Corée du Nord","Ukraine"]
canoe_kayak=["Hongrie","Slovaquie"]
cyclisme_sur_piste=["Royaume-Uni","Malaisie","Pays-Bas","Nouvelle-Zélande"]
cyclisme_sur_route=["Andorre","Australie","Autriche","Belgique","Burkina Faso","Colombie","Cuba","République tchèque","Danemark","Espagne","Estonie","France","Gabon","Allemagne","Irlande","Italie","Kazakhstan","Luxembourg","Pays-Bas","Qatar","Afrique du Sud","Russie","Slovénie","Suisse","Suède","Ukraine","Vénézuela"]
escalade=["Suisse"]
escrime=["France","Hongrie","Italie","Roumanie"]
football =["Afghanistan","Afrique du Sud", "Albanie","Algérie","Allemagne", "Andorre", "Angola", "Antilles néerlandaises", "Arabie saoudite", "Argentine", "Arménie","Aruba", "Autriche", "Azerbaïdjan", "Bahreïn","Bangladesh", "Biélorussie", "Belgique", "Belize", "Bénin", "Bolivie", "Bosnie-Herzégovine", "Botswana", "Brésil", "Brunei", "Bulgarie", "Burkina Faso", "Burundi", "Cambodge", "Cameroun", "Cap-Vert", "Chili", "Colombie", "Comores", "Congo", "Corée du Nord", "Costa Rica", "Côte d’Ivoire", "Chypre", "Croatie", "Danemark", "Djibouti", "Équateur", "Égypte", "El Salvador", "Érythrée", "Guinée équatoriale", "Éthiopie", "France", "Guyane française", "Gabon", "Gambie", "Géorgie", "Ghana", "Grèce", "Grenade", "Guatemala", "Guinée", "Guinée-Bissau", "Haïti", "Honduras", "Hongrie", "Indonésie", "Îles Salomon", "Iran", "Iraq", "Islande", "Israël", "Italie", "Jordanie", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Koweït", "Kirghizstan", "Laos", "Liban", "Lesotho", "Liberia", "Libye", "Liechtenstein", "Luxembourg", "Madagascar", "Malaisie", "Malawi", "Maldives", "Mali", "Malte", "Mauritanie", "Maurice", "Mexique", "Micronésie", "Moldavie", "Monaco", "Maroc", "Monténégro", "Mozambique", "Myanmar", "Namibie", "Niger", "Nigeria", "Macédoine du Nord", "Norvège", "Oman", "Ouganda", "Ouzbékistan", "Palestine", "Paraguay", "Pays-Bas", "Pérou", "Pologne"," Portugal", "Qatar", "République centrafricaine", "République démocratique du Congo", "Roumanie", "Royaume-Uni", "Russie", "Rwanda", "Saint-Kitts-et-Nevis", "Sainte-Lucie", "Saint-Marin", "São Tomé-et-Principe", "Sénégal", "Serbie", "Seychelles", "Sierra Leone", "Singapour", "Slovaquie", "Slovénie", "Somalie", "Soudan", "Soudan", "Suriname", "Suède", "Suisse", "Syrie", "Tadjikistan", "Tchad", "Tanzanie", "Thaïlande", "Timor-Leste", "Togo", "Tunisie", "Turquie", "Turkménistan", "Tuvalu", "Ukraine", "Uruguay", "Vanuatu", "Vietnam", "Yémen", "Zambie","Zimbabwe"]
golf=["Irlande","Japon","Corée du Sud","Afrique du Sud","Etats-Unis"]
gymnastique=["Chine","Roumanie"]
haltérophilie=["Bulgarie","Iles Caimans","Iran","Nauru","Tunisie"]
handball=["Algérie","Croatie","Danemark","Espagne","France","Allemagne","Islande","Roumanie","Russie","Serbie","Slovénie","Suisse","Suède","Handball"]
hockey_sur_gazon =["Bangladesh","Inde","Pays-Bas","Pakistan","Autorité palestinienne"]
judo = ["Algérie","Egypte","France","Georgie","Japon","Mongolie","Corée du Nord","Ouzbékistan"]
karaté=["Japon"]
lutte=["Azerbaijan","Bulgarie","Georgie","Iran","Kenya","Kirghizistan","Mongolie","Tadjikistan","Turkménistan","Tunisie","Ouzbékistan"]
natation=["Australie","France","Mexique","Monaco","Pays-Bas","Zimbabwe"]
natation_synchronisee=["Russie"]
plongeon=["Chine"]
rugby_a_7=["Autralie","Fidji","Royaume-Uni","Nouvelle-Zélande","Papouasie-Nouvelle-Guinée","Russie","Tonga"]
sports_equestres=["France","Royaume-Uni","Irlande","Japon","Mongolie","Emirats arabes unis","Etats-Unis"]
taekwondo=["Afghanistan","Corée du Sud","Corée du Nord"]
tennis=["Australie","Belgique","Chili","Chypre","Espagne","France","Monaco","Russie","Serbie","Suisse","Suède","Etats-Unis"]
tennis_de_table=["Cambodge","Chine","Corée du Sud","Singapour"]
tir=["Etats-Unis"]
tir_a_arc=["Bhoutan","Corée du Sud","Mongolie"]
voile =["Anguilla","Espagne","Royaume-Uni","Italie","Nouvelle-Zélande"]
volleyball=["Cambodge","Italie","Pologne","Sri Lanka"]
volleyball_de_plage=["Brésil"]
water_polo=["Hongrie","Serbie"]

Sports=[athletisme,aviron,badminton,basketball,boxe,canoe_kayak,cyclisme_sur_piste,cyclisme_sur_route,escalade,escrime,football,golf,gymnastique,handball,hockey_sur_gazon,haltérophilie,judo,karaté,lutte,natation,natation_synchronisee,plongeon,sports_equestres,taekwondo,tennis,tennis_de_table,tir,tir_a_arc,voile,volleyball,volleyball_de_plage,water_polo]

sports={"athlétisme":athletisme, "aviron":aviron,"badminton":badminton,"basketball":basketball,"boxe":boxe,"canoe-kayak":canoe_kayak,"cyclisme sur piste":cyclisme_sur_piste,"cyclisme sur route":cyclisme_sur_route,"escalade":escalade,"escrime":escrime,"football":football,"golf":golf,"gymnastique":gymnastique,"handball":handball,"hockey sur gazon":hockey_sur_gazon,"hatérophilie":haltérophilie,"judo":judo,"karaté":karaté,"lutte":lutte,"natation":natation,"natation synchronysée":natation_synchronisee,"plongeon":plongeon,"sports équestres":sports_equestres,"taekwondo":taekwondo,"tennis":tennis,"tennis de table":tennis_de_table,"tir":tir,"tir à l'arc":tir_a_arc,"voile":voile,"volleyball":volleyball,"volleyball de plage":volleyball_de_plage,"water polo":water_polo}