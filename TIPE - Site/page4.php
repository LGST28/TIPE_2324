<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <title>Find your match</title>
		<link rel="stylesheet" type="text/css" href="page4.css">
	</head>
	<body>
		<header> Find your match </header>
		<p> Choisissez vos sports </p>
		<p>&nbsp;</p>
		<form  action="<?php echo $_SERVER['PHP_SELF'];?>" method="post"/>
		 
		<button name= "handball" ><img src="pictogramme JO 2024/sports collectifs/handball.jpg"> <!--créer des images cliquables avec le poctogramme corespondant au sport--> 
		</br>
		<span> Handball</span>
		</button>
	    
		
		<button name= "3x3" ><img src="pictogramme JO 2024/sports collectifs/3x3 basketball.jpg">
		</br>
		<span>3x3 Basketball</span>
		</button>
		
		<button name= "basket" ><img src="pictogramme JO 2024/sports collectifs/basketball.jpg">
		</br>
		<span>Basketball</span>
		</button>
		
		
		<button name= "foot" ><img src="pictogramme JO 2024/sports collectifs/football.jpg">
		</br>
		<span>Football</span>
		</button>

		
		<button name= "hockey" ><img src="pictogramme JO 2024/sports collectifs/hockey.jpg">
		</br>
		<span>Hockey</span>
		</button>
		
		<button name= "rugby7" ><img src="pictogramme JO 2024/sports collectifs/rugby à sept.jpg">
		</br>
		<span>Rugby à sept</span>
		</button>
		
		
		<button name= "volley plage" ><img src="pictogramme JO 2024/sports collectifs/volleyball de plage.jpg">
		</br>
		<span>Volleyball de plage</span>
		</button>
		
		
		<button name= "volley" ><img src="pictogramme JO 2024/sports collectifs/volleyball.jpg">
		</br>
		<span>Volleyball</span>
		</button>
		
		
		<button onclick="openModal15()" name= "aviron" ><img src="pictogramme JO 2024/sport d'eau/aviron.jpg">
		</br>
		<span>Aviron</span>
		</button>
		<div id="modal15" class="modal">   <!--créer un pop-up avec les sous sports-->
		<div class="modal-content">
		<span class="close" onclick="closeModal15()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="Deux_de_couple" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Deux de couple</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Deux de couples poid léger</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Deux sans barreur</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Huit</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Quatre de couple</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Quatre sans barreur</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Skiff</label>
		</div>
		</div>
		</div>
		
		
		<button name= "canoe_course" ><img src="pictogramme JO 2024/sport d'eau/canoe course en ligne.jpg">
		</br>
		<span>Canoe course en ligne</span>
		</button>
		
		
		<button name= "canoe_slalom" ><img src="pictogramme JO 2024/sport d'eau/canoe kayak slalom.jpg">
		</br>
		<span>Canoe Kayak slalom</span>
		</button>
		
		
		<button name= "natation artistique" ><img src="pictogramme JO 2024/sport d'eau/natation artistique.jpg">
		</br>
		<span>Natation artistique</span>
		</button>
		
		
		<button name= "natation marathon" ><img src="pictogramme JO 2024/sport d'eau/natation marathon.jpg">
		</br>
		<span>Natation marathon</span>
		</button>
		
		
		<button name= "natation" ><img src="pictogramme JO 2024/sport d'eau/natation.jpg">
		</br>
		<span>Natation</span>
		</button>
		
		
		<button name= "plongeon" ><img src="pictogramme JO 2024/sport d'eau/plongeon.jpg">
		</br>
		<span>Plongeon</span>
		</button>
		
		
		<button name= "surf" ><img src="pictogramme JO 2024/sport d'eau/surf.jpg">
		</br>
		<span>Surf</span>
		</button>
		
		
		<button onclick="openModal14()" name= "voile" ><img src="pictogramme JO 2024/sport d'eau/voile.jpg">
		</br>
		<span>Voile</span>
		</button>
		<div id="modal14" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal14()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Dériveur</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Kitesurf</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Planche à voile</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Skiff</label>
		</div>
		</div>
		</div>
		
		
		<button name= "water-polo" ><img src="pictogramme JO 2024/sport d'eau/water-polo.jpg">
		</br>
		<span>Water-polo</span>
		</button>
		
		
		<button name= "breaking" ><img src="pictogramme JO 2024/gym-dance/breaking.jpg">
		</br>
		<span>Breaking</span>
		</button>
		
		
		<button name= "gymnastique artistique" ><img src="pictogramme JO 2024/gym-dance/gymnastique artistique.jpg">
		</br>
		<span>Gymnastique artistique</span>
		</button>
		
		
		<button name= "gymnastique rythmique" ><img src="pictogramme JO 2024/gym-dance/gymnastique rythmique.jpg">
		</br>
		<span>Gymnastique rythmique</span>
		</button>
		
		
		<button name= "gymnastique trampoline" ><img src="pictogramme JO 2024/gym-dance/gymnastique trampoline.jpg">
		</br>
		<span>Gymnastique trampoline</span>
		</button>
		
		
		<button onclick="openModal13()" name= "boxe" ><img src="pictogramme JO 2024/sports de combat/boxe.jpg">
		</br>
		<span>Boxe</span>
		</button>
		<div id="modal13" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal13()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids légers</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids lourds</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids mi-lourds</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids mouche</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids plumes</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids moyens</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids super-lourds</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Poids welters</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal12()"name= "judo" ><img src="pictogramme JO 2024/sports de combat/judo.jpg">
		</br>
		<span>Judo</span>
		</button>
		<div id="modal12" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal12()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 60kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 66kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 73kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 81kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 90kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 100kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Plus de 100kg</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal11()" name= "lutte" ><img src="pictogramme JO 2024/sports de combat/lutte.jpg">
		</br>
		<span>Lutte</span>
		</button>
		<div id="modal11" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal11()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Gréco-romaine</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Libre</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal10()" name= "taekwondo" ><img src="pictogramme JO 2024/sports de combat/taekwondo.jpg">
		</br>
		<span>Taekwondo</span>
		</button>
		<div id="modal10" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal10()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 58kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 68kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 80kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Plus de 80kg</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal9()" name= "badminton" onfocus="document.getElementById('menu_bad').style.display = 'block';" onblur="document.getElementById('menu_bad').style.display = 'none';"><img src="pictogramme JO 2024/sports de raquette/badminton.jpg">
		</br>
		<span>Badminton</span>
		</button>
		<div id="modal9" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal9()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Simple</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Double</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal8()" name= "ping pong" ><img src="pictogramme JO 2024/sports de raquette/tennis de table.jpg">
		</br>
		<span>Tennis de table</span>
		</button>
		<div id="modal8" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal8()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Individuel</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Equipe</label>
		</div>
		</div>
		</div>		
		
		
		<button onclick="openModal7()" name= "tennis" ><img src="pictogramme JO 2024/sports de raquette/tennis.jpg">
		</br>
		<span>Tennis</span>
		</button>
		<div id="modal7" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal7()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Simple</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Double</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal6()" name= "tir à l'arc" ><img src="pictogramme JO 2024/tir/tir à l'arc.jpg">
		</br>
		<span>Tir à l'arc</span>
		</button>
		<div id="modal6" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal6()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Individuel</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Equipe</label>
		</div>
		</div>
		</div>
		
		
		
		<button onclick="openModal5()" name= "tir" ><img src="pictogramme JO 2024/tir/tir.jpg">
		</br>
		<span>Tir</span>
		</button>
		<div id="modal5" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal5()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Carabine</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Fusil de chasse</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Carabine</label>
		</div>
		</div>
		</div>
		
		
		<button name= "BMX freestyle" ><img src="pictogramme JO 2024/vélo/BMX freestyle.jpg">
		</br>
		<span>BMX freestyle</span>
		</button>
		
		
		<button name= "BMX racing" ><img src="pictogramme JO 2024/vélo/BMX racing.jpg">
		</br>
		<span>BMX racing</span>
		</button>
		
		
		<button name= "cyclisme mountain bike" ><img src="pictogramme JO 2024/vélo/cyclisme mountain bike.jpg">
		</br>
		<span>Cyclisme mountain bike</span>
		</button>
		
		
		<button name= "cyclisme sur piste" ><img src="pictogramme JO 2024/vélo/cyclisme sur piste.jpg">
		</br>
		<span>Cyclisme sur piste</span>
		</button>
		
		
		<button name= "cyclisme sur route" ><img src="pictogramme JO 2024/vélo/cyclisme sur route.jpg">
		</br>
		<span>Cyclisme sur route</span>
		</button>
		
		
		<button name= "concours complet" ><img src="pictogramme JO 2024/équitation/concours complet.jpg">
		</br>
		<span>Concours complet</span>
		</button>
		
		
		<button name= "dressage" ><img src="pictogramme JO 2024/équitation/dressage.jpg">
		</br>
		<span>Dressage</span>
		</button>
		
		
		<button name= "saut d'obstacles" ><img src="pictogramme JO 2024/équitation/saut d'obstacles.jpg">
		</br>
		<span>Saut d'obstacles</span>
		</button>
		
		<button onclick="openModal4()" name= "athlétisme" onfocus="document.getElementById('menu_athle').style.display = 'block';" onblur="document.getElementById('menu_athle').style.display = 'none';"><img src="pictogramme JO 2024/autres/athlétisme.jpg">
		</br>
		<span>Athlétisme</span>
		</button>
		<div id="modal4" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal4()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">4x100m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">4x400m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">20km marche</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">100m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">110m haies</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">200m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">400m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">400m haies</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">800m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">1500m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">3000m steeple</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">5000m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">10000m</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Décathlon</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Lancer du disque</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Lancer du javelot</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Lancer du marteau</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Lancer du poids</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Marathon</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Saut à la perche</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Saut en hauteur</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Saut en longueur</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Triple saut</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal3()"name= "escalade" ><img src="pictogramme JO 2024/autres/escalade.jpg">
		</br>
		<span>Escalade</span>
		</button>
		<div id="modal3" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal3()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Combiné</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Vitesse</label>
		</div>
		</div>
		</div>
		
		
		<button onclick="openModal2()" name= "escrime" ><img src="pictogramme JO 2024/autres/escrime.jpg">
		</br>
		<span>Escrime</span>
		</button>
		<div id="modal2" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal2()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Epée</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Fleuret</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Sabre</label>
		</div>
		</div>
		</div>
		
		
		<button name= "golf" ><img src="pictogramme JO 2024/autres/golf.jpg">
		</br>
		<span>Golf</span>
		</button>
		
		
		<button onclick="openModal1()" name= "haltérophilie" ><img src="pictogramme JO 2024/autres/haltérophilie.jpg">
		</br>
		<span>Haltérophilie</span>
		</button>
		<div id="modal1" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal1()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 61kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 73kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 89kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Moins de 102kg</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Plus de 102kg</label>
		</div>
		</div>
		</div>
		
		
		
		<button name= "pentathlon moderne" ><img src="pictogramme JO 2024/autres/pentathlon moderne.jpg">
		</br>
		<span>Pentathlon moderne</span>
		</button>
		
		
		<button onclick= "openModal()" name= "skateboarding" ><img src="pictogramme JO 2024/autres/skateboarding.jpg">
		</br>
		<span>Skateboarding</span>
		</button>
		<div id="modal" class="modal">
		<div class="modal-content">
		<span class="close" onclick="closeModal()">&times;</span>
		<h3>Choissisez vos sous-sports</h3>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Park</label>
		</div>
		<div class="bouton">
		<input type="checkbox" id="sous_sport" name="sous sport" class="input"/>
		<label for="sous sport" class="label">Street</label>
		</div>
		</div>
		</div>


		
		
		<button name= "triathlon" ><img src="pictogramme JO 2024/autres/triathlon.jpg">
		</br>
		<span>Triathlon</span>
		</button>
		<p>&nbsp;</p>
		
		<input type=submit id="enregistrer" onchange="enregistrer()"; value="Valider" />
		</form>
		

		<script>
			function openModal() {                               
				document.getElementById("modal").style.display = "block";
				document.body.style.overflow = "hidden"; // Empêche le défilement de la page
			}
			function openModal1() {
				document.getElementById("modal1").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal2() {
				document.getElementById("modal2").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal3() {
				document.getElementById("modal3").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal4() {
				document.getElementById("modal4").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal5() {
				document.getElementById("modal5").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal6() {
				document.getElementById("modal6").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal7() {
				document.getElementById("modal7").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal8() {
				document.getElementById("modal8").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal9() {
				document.getElementById("modal9").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal10() {
				document.getElementById("modal10").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal11() {
				document.getElementById("modal11").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal12() {
				document.getElementById("modal12").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal13() {
				document.getElementById("modal13").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal14() {
				document.getElementById("modal14").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}
			function openModal15() {
				document.getElementById("modal15").style.display = "block";
				document.body.style.overflow = "hidden"; 
			}


			function closeModal() {
				document.getElementById("modal").style.display = "none";
				document.body.style.overflow = "auto"; // Réactive le défilement de la page
			}
			function closeModal1() {
				document.getElementById("modal1").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal2() {
				document.getElementById("modal2").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal3() {
				document.getElementById("modal3").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal4() {
				document.getElementById("modal4").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal5() {
				document.getElementById("modal5").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal6() {
				document.getElementById("modal6").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal7() {
				document.getElementById("modal7").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal8() {
				document.getElementById("modal8").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal9() {
				document.getElementById("modal9").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal10() {
				document.getElementById("modal10").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal11() {
				document.getElementById("modal11").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal12() {
				document.getElementById("modal12").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal13() {
				document.getElementById("modal13").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal14() {
				document.getElementById("modal14").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			function closeModal15() {
				document.getElementById("modal15").style.display = "none";
				document.body.style.overflow = "auto"; 
			}
			
﻿
	</script>
	<?php 
	
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		if(isset($_POST['enregistrer'])){
		$texte=file_get_contents('utilisateur.csv');
		$texte .= "\nSports:\nSous_sports";		
		file_put_contents('utilisateur.csv',$texte);
	 if(isset($_POST['Deux_de_couple'])){
		 $texte.= " Deux_de_couple";
		 file_put_contents('utilisateur.csv',$texte);
	 }
	 if(isset($_POST['feminin'])){
		 $texte.=" Feminin";
		 file_put_contents('utilisateur.csv',$texte);
	 }
	 if(isset($_POST['mixte'])){
		 $texte.=" Mixte";
		 file_put_contents('utilisateur.csv',$texte);
	 }
	 header('Location: page4.php');
	 exit();
	}
	}
	?>
	</body>
	</html>