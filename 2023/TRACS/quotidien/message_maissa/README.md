***** DESCRIPTION *****************************************************************************************************************************************

Une experte en attaque par canaux auxiliaires, Jmouinzin Maissa, qui travaillait sur un projet important, est projetée en urgence sur une mission encore plus prioritaire. Avant de partir elle confie les données concernant le projet à un collègue chargé de finir le travail.

Ce projet consiste à retrouver la clef secrète de 2048 bits d’un dispositif de chiffrement.
Ce dispositif accepte plusieurs commandes, dont notamment :


    - “cipher” : qui permet de chiffrer des messages avec la clef secrète (mais sans avoir besoin de rentrer cette clef secrète car elle est stockée dans le dispositif).

    - “root” : qui permet de prendre totalement le contrôle du dispositif. Pour cela il faut rentrer la clef secrète (la même que celle qui est utilisée par le dispositif lors de la commande de “cipher”). Or, après trois échecs consécutifs, le dispositif se verrouille définitivement.


Les données sont :


    quelques bouts de code de l’algorithme de chiffrement utilisé par le disposif.

    cinq fichiers d’analyse créés par l’experte avant son départ. Chacun de ces fichiers contient :

        le module utilisé pour le chiffrement (c’est une donnée connue, contrairement à la clef secrète, et qui ne varie pas),

        le message qui a été choisi par l’experte pour être chiffré par le dispositif avec la commande “cipher”,

        et enfin la courbe de consommation de courant mesurée sur le dispositif lors de ce chiffrement.




Le collègue chargé de terminer le projet, pensant tenir la solution, teste une clef commençant par les bits 0100011011 et terminant par les bits 1101111110, mais c’est un échec. Il a dans l’idée de tester le complémentaire de cette clef mais il se retient au dernier moment en songeant qu’il ne reste plus que deux essais. Plus sagement, il se dit que ce qu’il a tenté était sans doute un peu trop naïf et il vous appelle à la rescousse pour l’aider à ne pas gâcher les deux derniers essais.
***************************************************************************************************************************************************************************
