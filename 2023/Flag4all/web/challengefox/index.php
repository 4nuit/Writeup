<?php
include "flag.php";

$variable = $_GET["variable"];
$secretflag = "Le drapeau secret";

echo "<title>Challenge Fox</title>";
echo "<b>Challenge Fox</b>";
echo "<p>Analyser le code ci-dessous et trouver le moyen d'afficher le flag.</p>";

$query = urldecode($_SERVER["QUERY_STRING"]);

if (preg_match("/ |_/", $query)) {
    echo "Echec. <br />";
    source();
    exit;
}

if ($variable === "challengefox") {
    echo "- Si ce texte apparaît, tu valides la première étape! <br>";
    
    if (isset($_GET["challenge_fox"])) {
        echo "- Deuxième étape validée! <br>";
        
        if (hash("md2", $_GET["variable2"]) == "0") {
            echo "- Troisième étape validée! <br>";
            
            if (hash("sha1", $_GET["variable3"]) == $_GET["variable3"]) {
                echo "- Okay, voici le flag : " . $secretflag . "<br>";
            }
        }
    }
}

function source() {
    echo "<br><code>";
    highlight_string(file_get_contents(__FILE__));
    echo "</code>";
}
?>
