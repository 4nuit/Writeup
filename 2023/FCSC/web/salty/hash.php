<?php

$password = "H";
$hash = hash('fnv164',$password);
echo $hash;
echo "\n";
?>
