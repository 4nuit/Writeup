<?php

$counter = 0;
while (1) {
    $p = '9be4a60f645f' . bin2hex(random_bytes(12));
    $counter += 1;
    if (hash('fnv164', $p) == 0) {
        $h = hash('fnv164', $p); 
        echo $p;
        echo "\n";
        echo $h;
        echo "\n";
        echo $counter;
        exit();
    }
}
?>
