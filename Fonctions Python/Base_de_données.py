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
    

athletisme = points( "athletisme" , ["Antilles néerlandaises","DZA","BHS","BEL","BHR","Iles Caimans","CMR","CRI","CUB","DOM","ECU","ERI","EST","ETH","FIN","FRA","GBR","GRC","JAM","KEN","LVA","MAR","NGA","NZL","PAN","POL","PRT","QAT","ZEF","Russie","Somalie","Suède","TZN","TTO","TUN","UKR"], ["USA","KEN","JAM","ETH","GBR"])
aviron= points("aviron",["CAN","DNK","GBR","POL"],["Pays-Bas","GBR","Italie","USA","ROU"])
badminton= points( "badminton" ,["CHN","IDN","MYS","SGP","THA"],["CHN","KOR","JPN","DNK","IDN"])
basketball= points("basketball", ["Angola","ARG","BHS","BIH","CHN","KOR","HRV","ESP","EST","FRA","GRC","ISR","Italie","Liban","Lituanie","PHL","Russie","Serbie","SGP","Slovénie","Soudan du Sud","TUN","USA"],["Allemagne","Serbie","USA","CAN","Lituanie"])
boxe= points("boxe", ["Azerbaidjan","CRI","Iralnde","Moldavie","MEX","Maurice","PHL","Corée du Nord","UKR"],["Ouzbékistan","KAZ","Russie","CUB","IND"])
canoe_kayak= points("canoe_kayak", ["HUN","Slovaquie"],["Allemagne","HUN","ESP","POL","CAN","GBR","FRA","République Tchèque","Slovénie","AUS"])
bmx = points("bmx", [] , ["FRA","GBR","CHN","USA","AUS"])
cyclisme_sur_piste= points("cyclisme_sur_piste" , ["GBR","MYS","Pays-Bas","NZL"],["GBR","Allemagne","Pays-Bas","AUS","Nouvelle Zélande"])
cyclisme_sur_route= points( "cyclimse_sur_route", ["Andorre","AUS","Autriche","BEL","BFA","COL","CUB","République tchèque","DNK","ESP","EST","FRA","Gabon","Allemagne","Irlande","Italie","KAZ","Luxembourg","Pays-Bas","QAT","ZEF","Russie","Slovénie","Suisse","Suède","UKR","Vénézuela"],["Pays-Bas","BEL","GBR","DNK","USA"])
escalade= points("escalade" , ["Suisse"],["JPN","USA","FRA","Autriche","Slovénie"])
escrime= points ("escrime" ,["FRA","HUN","Italie","ROU"],["Italie","FRA","HUN","JPN","USA"])
football = points("football" , ["Afghanistan","ZEF", "Albanie","DZA","Allemagne", "Andorre", "Angola", "Antilles néerlandaises", "SAU", "ARG", "Arménie","Aruba", "Autriche", "Azerbaïdjan", "Bahreïn","Bangladesh", "Biélorussie", "BEL", "Belize", "Bénin", "BOL", "BIH", "Botswana", "BRA", "Brunei", "Bulgarie", "BFA", "Burundi", "Cambodge", "CMR", "Cap-Vert", "Chili", "COL", "Comores", "Congo", "Corée du Nord", "CRI", "Côte d’Ivoire", "Chypre", "HRV", "DNK", "DJI", "Équateur", "Égypte", "El Salvador", "Érythrée", "Guinée équatoriale", "Éthiopie", "FRA", "Guyane française", "Gabon", "Gambie", "Géorgie", "Ghana", "GRC", "Grenade", "GTM", "Guinée", "Guinée-Bissau", "Haïti", "Honduras", "HUN", "IDN", "Îles Salomon", "IRN", "Iraq", "Islande", "Israël", "Italie", "Jordanie", "KAZ", "KEN", "Kiribati", "Kosovo", "Koweït", "Kirghizstan", "Laos", "Liban", "Lesotho", "Liberia", "Libye", "Liechtenstein", "Luxembourg", "Madagascar", "MYS", "Malawi", "Maldives", "Mali", "Malte", "Mauritanie", "Maurice", "MEX", "Micronésie", "Moldavie", "Monaco", "MAR", "Monténégro", "Mozambique", "Myanmar", "Namibie", "Niger", "NGA", "Macédoine du Nord", "Norvège", "Oman", "UGA", "Ouzbékistan", "Palestine", "Paraguay", "Pays-Bas", "PER", "POL"," PRT", "QAT", "République centrafricaine", "République démocratique du Congo", "ROU", "GBR", "Russie", "Rwanda", "Saint-Kitts-et-Nevis", "Sainte-Lucie", "Saint-Marin", "São Tomé-et-Principe", "Sénégal", "Serbie", "Seychelles", "Sierra Leone", "SGP", "Slovaquie", "Slovénie", "Somalie", "Soudan", "Soudan", "SUR", "Suède", "Suisse", "Syrie", "Tadjikistan", "Tchad", "TZN", "Thaïlande", "Timor-Leste", "Togo", "TUN", "Turquie", "Turkménistan", "Tuvalu", "UKR", "URY", "Vanuatu", "VNM", "Yémen", "Zambie","ZWE"],["ESP","ARG","FRA","GBR","Suède"])
golf= points("golf" , ["Irlande","JPN","KOR","ZEF","USA"],["USA","GBR","KOR","ESP","AUS"])
gymnastique= points("gymnastique" , ["CHN","ROU"],["USA","JPN","CHN","GBR","BRA","ISR","Italie","Allemagne","Bulagrie","ESP"])
haltérophilie= points( "haltérophilie", ["Bulgarie","Iles Caimans","IRN","Nauru","TUN"],["CHN","COL","KOR","Arménie","THA"])
handball= points("handball",["DZA","HRV","DNK","ESP","FRA","Allemagne","Islande","ROU","Russie","Serbie","Slovénie","Suisse","Suède","Handball"],["DNK","FRA","ESP","Suède","Allemagne"])
hockey_sur_gazon = points("hockey_sur_gazon",["Bangladesh","IND","Pays-Bas","PAK","Autorité palestinienne"], [])
judo = points("judo",["DZA","EGY","FRA","Georgie","JPN","Mongolie","Corée du Nord","Ouzbékistan"],["JPN","FRA","Géorgie","Italie","Ouzbékistan"])
karaté= points("karaté",["JPN"],["JPN","EGY","Italie","ESP","FRA"])
lutte= points("lutte",["Azerbaijan","Bulgarie","Georgie","IRN","KEN","Kirghizistan","Mongolie","Tadjikistan","Turkménistan","TUN","Ouzbékistan"],["USA","JPN","IRN","Turquie","Géorgie"])
natation= points("natation", ["AUS","FRA","MEX","Monaco","Pays-Bas","ZWE"],["USA","AUS","CHN","GBR","CAN"])
natation_synchronisee= points("natation_synchronisee",["Russie"],["JPN","ESP","CHN","Autriche","GBR"])
pentathlon = points("pentathlon" , [] , ["EGY","Italie","GBR","MEX","KOR"])
plongeon= points("plongeon",["CHN"],["CHN","MEX","AUS","GBR","CAN"])
rugby_a_7= points("rugby_a_7",["Autralie","FJI","GBR","NZL","Papouasie-Nouvelle-Guinée","Russie","Tonga"], [])
skateboard = points("skateboard" , [] , ["JPN","BRA","USA","AUS","GBR"])
sports_equestres= points("sports_equestres",["FRA","GBR","Irlande","JPN","Mongolie","ARE","USA"],["GBR","Allemagne","Suède","Pays-Bas","DNK"])
surf = points("surf", [] , ["BRA","AUS","USA","FRA","JPN"])
taekwondo= points("taekwondo",["Afghanistan","KOR","Corée du Nord"],["HRV","Turquie","KOR","Ouzbékistan","GBR"])
tennis= points("tennis", ["AUS","BEL","Chili","Chypre","ESP","FRA","Monaco","Russie","Serbie","Suisse","Suède","USA"],["USA","Serbie","République Tchèque","ESP","POL"])
tennis_de_table= points("tennis_de_table",["Cambodge","CHN","KOR","SGP"],["CHN","JPN","KOR","Allemagne","Suède"])
tir= points("tir",["USA"],["CHN","USA","KOR","IND","UKR"])
tir_a_arc= points("tir_a_arc",["Bhoutan","KOR","Mongolie"],["IND","KOR","Pays-Bas","MEX","Turquie"])
trampoline = points("trampoline", [] , ["GBR","USA","AUS","FRA","PRT"])
triathlon = points("triathlon", [] , ["FRA","GBR","Nouvelle Zélande","PRT","USA"])
voile = points("voile",["Anguilla","ESP","GBR","Italie","NZL"],["GBR","Pays-Bas","Italie","ISR","FRA"])
volleyball= points("volleyball",["Cambodge","Italie","POL","Sri Lanka"],["POL","USA","Turquie","JPN","Italie"])
volleyball_de_plage= points("volleyball_de_plage",["BRA"],["BRA","CAN","Norvège","USA","Allemagne"])
vtt = points("vtt", [] , ["FRA","GBR","Suisse","Autriche","Nouvelle Zélande"])
water_polo= points("water_polo",["HUN","Serbie"] , [])

Sports=[athletisme,aviron,badminton,basketball,boxe,canoe_kayak,cyclisme_sur_piste,cyclisme_sur_route,escalade,escrime,football,golf,gymnastique,handball,hockey_sur_gazon,haltérophilie,judo,karaté,lutte,natation,natation_synchronisee,plongeon,sports_equestres,taekwondo,tennis,tennis_de_table,tir,tir_a_arc,voile,volleyball,volleyball_de_plage,water_polo]

sports={"athlétisme":athletisme.pays_prefs, "aviron":aviron.pays_prefs,"badminton":badminton.pays_prefs,"basketball":basketball.pays_prefs,"boxe":boxe.pays_prefs,"canoe-kayak":canoe_kayak.pays_prefs,"cyclisme sur piste":cyclisme_sur_piste.pays_prefs,"cyclisme sur route":cyclisme_sur_route.pays_prefs,"escalade":escalade.pays_prefs,"escrime":escrime.pays_prefs,"football":football.pays_prefs,"golf":golf.pays_prefs,"gymnastique":gymnastique.pays_prefs,"handball":handball.pays_prefs,"hockey sur gazon":hockey_sur_gazon.pays_prefs,"hatérophilie":haltérophilie.pays_prefs,"judo":judo.pays_prefs,"karaté":karaté.pays_prefs,"lutte":lutte.pays_prefs,"natation":natation.pays_prefs,"natation synchronysée":natation_synchronisee.pays_prefs,"plongeon":plongeon.pays_prefs,"sports équestres":sports_equestres.pays_prefs,"taekwondo":taekwondo.pays_prefs,"tennis":tennis.pays_prefs,"tennis de table":tennis_de_table.pays_prefs,"tir":tir.pays_prefs,"tir à l'arc":tir_a_arc.pays_prefs,"voile":voile.pays_prefs,"volleyball":volleyball.pays_prefs,"volleyball de plage":volleyball_de_plage.pays_prefs,"water polo":water_polo.pays_prefs}

best_sports={"athlétisme":athletisme.best,"aviron":aviron.best,"badminton":badminton.best,"basketball":basketball.best,"BMX":bmx.best,"boxe":boxe.best,"canoe-kayak slalom":canoe_kayak.best,"canoe-kayak sprint":canoe_kayak.best,"cyclisme de route":cyclisme_sur_route.best,"cyclisme sur piste":cyclisme_sur_piste.best,"VTT":vtt.best,"escalade":escalade.best,"escrime":escrime.best,"football":football.best,"golf":golf.best,"gymnastique":gymnastique.best,"gymnastique rythmique":gymnastique.best,"haltérophilie":haltérophilie.best,"handball":handball.best,"judo":judo.best,"karaté":karaté.best,"lutte":lutte.best,"natation":natation.best,"natation synchronisée":natation.best,"pentathlon moderne":pentathlon.best,"plongeon":plongeon.best,"skateboard":skateboard.best,"sports équestres":sports_equestres.best,"surf":surf.best,"taekwondo":taekwondo.best,"tennis":tennis.best,"tennis de table":tennis_de_table.best,"tir":tir.best,"trampoline":trampoline.best,"triathlon":triathlon.best,"voile":voile.best,"volleyball":volleyball.best,"volley de plage":volleyball_de_plage.best}