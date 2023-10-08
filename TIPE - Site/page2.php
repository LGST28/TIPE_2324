<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <title>Find your match</title>
		<link rel="stylesheet" type="text/css" href="page2.css">
		<link rel="stylesheet" type="text/css" href="style_calendrier.css">
		<script src= "jquery-1.12.4.js"></script>  <!--bibliothèque jquery pour faire le calendrier-->
		<script src= "jquery-ui.js"></script>
	
    </head>
	<body>
		<header> Find your match </header>
        <p>rentrez vos dates de départ et d'arrivé sur Paris</p>
		<p id= a> Date d'arrivée </p> <p id= d> Date de départ </p>
		<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post"/>
		<input type="text" id="date_arrivée" name="date_arrivée" onchange="ord('date_arrivée')" class="content-editable"/>   
		<input type="text" id="date_départ" name="date_départ" onchange = "ord('date_départ')" class="content-editable"/>
		<input type=submit id="enregistrer" name="enregistrer"  class="date-enregistrer" value="Valider" />
		</form>
	<script type="text/javascript" language="javascript">
	$("#date_arrivée").datepicker();        <!-- créer le calendrier-->
	$("#date_départ").datepicker();
	
	function ord (nom){
		var txt = document.getElementById(nom).value;
		txt = txt.substr(3,3) + txt.substr(0,2)     <!-- permet de mettre la date de manière française et plus en manière américaine et de réduire à uniquement jour et mois(+ txt.substr(6); si on veut rajouter l'année)-->
		document.getElementById(nom).value = txt;
		}		
	</script>

		  
<!--fonction PHP qui va chercher le contenu des bouton date_arrivée et date_départ et qui les enregistrent dans un fichier texte  + qui redirige vers la page3-->
<?php 

if ($_SERVER["REQUEST_METHOD"] == "POST") {   
	$filename = "utilisateur.csv";
	$file = fopen($filename, "w");
	if ($file) {
		fwrite($file, 'Date: ');
		fwrite($file, $_POST['date_arrivée']);
		fwrite($file, ' ');
		fwrite($file, $_POST['date_départ']);
		fclose($file);
	} else {
	    $error = error_get_last();
		echo "Erreur lors de l'ouverture du fichier : " . $error['message'];
} 
  header('Location: page3.php');
  exit();
}

?>




</body>	
</html>

