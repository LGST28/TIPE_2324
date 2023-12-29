
#################################################################################
# Ce fichier regroupe l'ensemble des données et foncitons liées à l'utilisateur #
#################################################################################

# Commençons par introduire la forme des données que nous manipulons

donnees = [ [ [] ], # Préférence des sports (5 tableaux de tableaux à 2 éléments, à savoir le nom du sport et la note attribuée)
            [], # Préférence de genre (Entier = 0 pour non, entier = 1 pour femme de préférence, entier = 2 pour homme de préférence)
            [], # Souhait d'avoir d'autres sports que les sports sélectionnés
            [], # Préférence pour le type de rencontre (Associer un entier ou chaine de caractère en fonction du type de rencontre)
            [], # Dates d'arrivée et de départ (tableau à deux éléments)
            [], # Préférence de dates strictes (entier = 0) ou larges (entier = nombre de jours à prendre en compte)
            [], # Préférence d'emploi du temps, entier (= 0 pour quantité, = 1 pour qualité)
            [], # Nationnalité (Chaine de caractère type : FRA, BEL, USA)
            [], # Préférence de nationnalité
            [], # Capacité au déplacement
             ]  

####################################
# Base de données des nationalites #
####################################


class nationnalite:
    
    def __init__(self, abreviation, region):
        self.abreviation = abreviation
        self.region = region



Afrique_du_sud = nationnalite("ZEF" , "Afrique")
Algerie = nationnalite("DZA" , "Afrique")
Burkina_Faso = nationnalite("BFA", "Afrique")
Cameroun = nationnalite("CMR", "Afrique")
Djibouti = nationnalite("DJI", "Afrique")
Egypte = nationnalite("EGY", "Afrique")
Erythree = nationnalite("ERI", "Afrique")
Ethiopie = nationnalite("ETH", "Afrique")
Gambie = nationnalite("GMB", "Afrique")
Kenya = nationnalite("KEN", "Afrique")
Maroc = nationnalite("MAR", "Afrique")
Nigeria = nationnalite("NGA", "Afrique")
Ouganda = nationnalite("UGA", "Afrique")
Senegal = nationnalite("SEN", "Afrique")
Tanzanie = nationnalite("TZN", "Afrique")
Tunisie = nationnalite("TUN", "Afrique")
Zimbabwe = nationnalite("ZWE", "Afrique")
Australie = nationnalite("AUS", "Oceanie")
Fidji = nationnalite("FJI", "Oceanie")
Nouvelle_Zelande = nationnalite("NZL", "Oceanie")
Argentine = nationnalite("ARG" , "Ameriques")
Bolivie = nationnalite("BOL" , "Ameriques")
Bresil = nationnalite("BRA" , "Ameriques")
Canada = nationnalite("CAN" , "Ameriques")
Colombie = nationnalite("COL" , "Ameriques")
Costa_Rica = nationnalite("CRI" , "Ameriques")
Cuba = nationnalite("CUB" , "Ameriques")
Equateur = nationnalite("ECU" , "Ameriques")
Etats_Unis = nationnalite("USA" , "Ameriques")
Guatemala = nationnalite("GTM" , "Ameriques")
Jamaique = nationnalite("JAM" , "Ameriques")
Mexique = nationnalite("MEX" , "Ameriques")
Perou = nationnalite("PER" , "Ameriques")
Porto_Rico = nationnalite("PRI" , "Ameriques")
Republique_Dominicaine = nationnalite("DOM" , "Ameriques")
Suriname = nationnalite("SUR" , "Ameriques")
Trinite_et_Tobago = nationnalite("TTO" , "Ameriques")
Uruguay = nationnalite("URY" , "Ameriques")
Arabie_Saoudite = nationnalite("SAU" , "Asie")
Bahrein = nationnalite("BHR" , "Asie")
Chine = nationnalite("CHN" , "Asie")
Coree_du_sud = nationnalite("KOR", "Asie")
Emirats_arabes_unis = nationnalite("ARE" , "Asie")
Hong_Kong = nationnalite("HNK" , "Asie")
Inde = nationnalite("IND" , "Asie")
Iran = nationnalite("IRN" , "Asie")
Israel = nationnalite("ISR" , "Asie")
Japon = nationnalite("JPN" , "Asie")
Kazakhstan = nationnalite("KAZ" , "Asie")
Pakistan = nationnalite("PAK" , "Asie")
Philippines = nationnalite("PHL" , "Asie")
Qatar = nationnalite("QAT" , "Asie")
Singapour = nationnalite("SGP" , "Asie")
Tapei_chinois = nationnalite("TAP" , "Asie")
Vietnam = nationnalite("VNM" , "Asie")
Allemagne = nationnalite("DEU", "Europe")
Armenie = nationnalite("ARM", "Europe")
Autriche = nationnalite("AUT", "Europe")
Azerbaidjan = nationnalite("AZE", "Europe")
Belgique = nationnalite("BEL", "Europe")
Bosnie_Herzegovine = nationnalite("BIH", "Europe")
Bulgarie = nationnalite("BGR", "Europe")
Croatie = nationnalite("HRV", "Europe")
Danemark = nationnalite("DNK", "Europe")
Espagne = nationnalite("ESP", "Europe")
Estonie = nationnalite("EST", "Europe")
Finlande = nationnalite("FIN", "Europe")
France = nationnalite("FRA", "Europe")
Georgie = nationnalite("GEO", "Europe")
Grande_Bretagne = nationnalite("GBR", "Europe")
Grece = nationnalite("GRC", "Europe")
Hongrie = nationnalite("HUN", "Europe")
Irlande = nationnalite("IRL", "Europe")
Italie = nationnalite("ITA", "Europe")
Lituanie = nationnalite("LTU", "Europe")
Moldavie = nationnalite("MDA", "Europe")
Norvege = nationnalite("NOR", "Europe")
Pays_Bas = nationnalite("NLD", "Europe")
Pologne = nationnalite("POL", "Europe")
Portugal = nationnalite("PRT", "Europe")
Roumanie = nationnalite("ROU", "Europe")
Serbie = nationnalite("SCG", "Europe")
Slovaquie = nationnalite("SVK", "Europe")
Slovenie = nationnalite("SVN", "Europe")
Suede = nationnalite("SWE", "Europe")
Tchequie = nationnalite("CZE", "Europe")
Turquie = nationnalite("TUR", "Europe")
Ukraine = nationnalite("UKR", "Europe")


Abreviations = {"Afrique du sud": Afrique_du_sud.abreviation, "Algerie": Algerie.abreviation, "Burkina Faso": Burkina_Faso.abreviation, "Cameroun": Cameroun.abreviation, "Djibouti": Djibouti.abreviation, "Egypte": Egypte.abreviation, "Erythree": Erythree.abreviation,
                "Ethiopie": Ethiopie.abreviation, "Gambie": Gambie.abreviation, "Kenya": Kenya.abreviation, "Maroc": Maroc.abreviation, "Nigeria": Nigeria.abreviation, "Ouganda": Ouganda.abreviation, "Senegal": Senegal.abreviation, "Tanzanie": Tanzanie.abreviation, 
                "Tunisie": Tunisie.abreviation, "Zimbabwe": Zimbabwe.abreviation, "Australie": Australie.abreviation, "Fidji": Fidji.abreviation, "Nouvelle_Zelande": Nouvelle_Zelande.abreviation, "Argentine": Argentine.abreviation, "Bolovie": Bolivie.abreviation,
                " Bresil": Bresil.abreviation, "CAN": Canada.abreviation, "Colombie": Colombie.abreviation, "Costa_Rica": Costa_Rica.abreviation, "Cuba": Cuba.abreviation, "Equateur": Equateur.abreviation, "Etats_Unis": Etats_Unis.abreviation, "Guatemala": Guatemala.abreviation,
                "Jamaique": Jamaique.abreviation, "MEX": Mexique.abreviation, "Perou": Perou.abreviation, "Porto_Rico": Porto_Rico.abreviation, "Republique_Dominicaine": Republique_Dominicaine.abreviation, "Suriname" : Suriname.abreviation, "Trinite_et_Tobago": Trinite_et_Tobago.abreviation,
                "Uruguay": Uruguay.abreviation, "Arabie_Saoudite": Arabie_Saoudite.abreviation, "Bahrein": Bahrein.abreviation, "Chine": Chine.abreviation, "Coree_du_sud": Coree_du_sud.abreviation,  "Emirats_arabes_unis": Emirats_arabes_unis.abreviation, "Hong_Kong": Hong_Kong.abreviation,
                "Inde": Inde.abreviation, "Iran": Iran.abreviation, "Israel": Israel.abreviation, "Japon": Japon.abreviation, "Kazakhstan": Kazakhstan.abreviation, "Pakistan": Pakistan.abreviation, "Philippines": Philippines.abreviation, "Quatar": Qatar.abreviation,
                "Singapour": Singapour.abreviation, "Tapei_chinois": Tapei_chinois.abreviation, "Vietnam": Vietnam.abreviation, "Allemagne": Allemagne.abreviation, "Armenie": Armenie.abreviation, "Autriche": Autriche.abreviation, "Azerbaidjan": Azerbaidjan.abreviation,
                "Belgique": Belgique.abreviation, "Bosnie_Herzegovine": Bosnie_Herzegovine.abreviation, "Bulgarie": Bulgarie.abreviation, "Croatie": Croatie.abreviation, "Danemark": Danemark.abreviation, "Espagne": Espagne.abreviation, "Estonie": Estonie.abreviation,
                "Finland": Finlande.abreviation, "France": France.abreviation, "Georgie": Georgie.abreviation, "Grande_Bretagne": Grande_Bretagne.abreviation, "Grece": Grece.abreviation, "Hongrie": Hong_Kong.abreviation, "Irlande": Irlande.abreviation, 
                "Italie": Italie.abreviation, "Lituanie": Lituanie.abreviation, "Moldavie": Moldavie.abreviation, "Norvege": Norvege.abreviation, "Pays_Bas": Pays_Bas.abreviation, "Pologne": Pologne.abreviation, "Portugal": Porto_Rico.abreviation, "Roumanie": Roumanie.abreviation,
                "Serbie": Serbie.abreviation, "Slovaquie": Slovaquie.abreviation, "Slovenie": Slovenie.abreviation, "Suede": Suede.abreviation, "Tchequie": Tchequie.abreviation, "Turquie": Turquie.abreviation, "Ukraine": Ukraine.abreviation}


##########################
# Fonctions nationnalité #
##########################

# Fonction qui vérifie