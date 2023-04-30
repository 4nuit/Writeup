<?php

$counter =0;
while(1){
    $p = bin2hex(random_bytes(18));
    $counter+=1;
    if (hash('fnv164',$p)==0) {

        $h = hash('fnv164',$p); 
        echo $p;
        echo "\n";
        echo $h;
        echo "\n";
        echo $counter;
        exit();

    }
}

?>
