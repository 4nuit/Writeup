<?php

while(1){
	$p = bin2hex(random_bytes(18));
	if (hash('fnv164',$p)==0){
		$h = hash('fnv164',$p)==0;
		echo $p;
		echo $h;
		exit();
	}
}
?>
