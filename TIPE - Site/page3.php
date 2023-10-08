<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <title>Find your match</title>
		<link rel="stylesheet" type="text/css" href="page3.css">
	</head>
	<body>
		<header> Find your match </header>
		<p> Choisissez le genre </p>
		<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post"/>
		<div>
        <input type="checkbox" id="masculin" name="masculin"/>
        <label for="masculin">Masculin</label>
		</div>

		<div>
		<input type=submit id="enregistrer" onchange="enregistrer()" value="Valider" />  <input type="checkbox" id="feminin" name="feminin"/> 
		<label for="feminin">Féminin</label>
		</div>
		
		<div>
		<input type="checkbox" id="mixte" name="mixte"/>
        <label for="mixte">Mixte</label>
		</div>
		</form>
	<?php 
	
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$texte=file_get_contents('utilisateur.csv');    // fonction qui enregistre dans le fichier texte
		$texte .= "\nGenres:";
		file_put_contents('utilisateur.csv',$texte);
	 if(isset($_POST['masculin'])){
		 $texte.= " Masculin";
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
	?>
		
		
	</body>
	
</html>
