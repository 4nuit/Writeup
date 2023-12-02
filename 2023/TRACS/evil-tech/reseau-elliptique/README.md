**** DESCRIPTION *****************************************************************************************************************************************

Les employés d’EvilTech utilisent, pour communiquer entre eux, un logiciel basé sur un échange de clef sur une courbe elliptique. Celle-ci peut être changée par les utilisateurs pour prendre celle de leur choix.
Chaque courbe elliptique est définie par 3 paramètres : a, b et p et les points la constituant sont tels que x³ + ax + b = y² modulo p. De plus, ces paramètres sont des grands nombres sur 256 bits, a priori inconnus, et nous savons que p est un nombre premier généré aléatoirement entre (2²⁵⁶ - 2¹⁹²) et 2²⁵⁶.
Nous pouvons nous attendre à ce que des utilisateurs faisant partis d’un même réseau utilisent la même courbe. Aussi, nous avons collecté un certain nombre de points constituant les clefs publiques des utilisateurs et souhaiterions retrouver un maximum d’entre eux utilisant la même courbe qu’evilboy, le pseudo d’un employé d’EvilTech.
***************************************************************************************************************************************************************************
