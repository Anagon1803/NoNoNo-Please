label library:

    scene bg library

    "Cette étagère a plein de livres «BIOGRAPHIQUES», grand-père était un homme de culture."

    if cosmo_mission == 1 and not cosmo_book:
        "Chercher dans tous ces livres va me prendre 1 unité de temps."

        menu:
            "Fouiller":
                $ cosmo_book = True
                $ time_units -= 1
                "Après avoir fouillé un moment, je finis par trouver un exemplaire de ‘La Phytophilie chez les elfes sylvains’."

                "Chercher un livre alors qu’on a la 5G, faut vraiment être mort pour faire ce genre de chose."

            "Ne pas fouiller":
                "Flemme."

    jump free_move_library

label flower_bed:

    scene bg garden

    "C’est un joli parterre de fleurs."

    if cosmo_mission == 1 and not cosmo_war:
        "Cosmo veut que je règle un conflit géopolitique ici."

        menu:
            "Arracher à la main (3 unités de temps)":
                $ cosmo_war = True
                $ time_units -= 3
                "C’était chiant, mais c’est fait !"

            "Utiliser les cisailles (1 unité de temps)" if shears_inventory:
                $ cosmo_war = True
                $ time_units -= 1
                "C’était pas si chiant à faire en réalité."

            "Utiliser la pelle (1 unité de temps)" if shovel_inventory:
                $ cosmo_war = True
                $ time_units -= 1
                $ shovel_inventory = 2
                "Paix à l’âme de cette pelle qui a rompu durant le combat, mais les tulipes sont triomphantes !"

            "Ne pas intervenir":
                "Flemme."

    jump free_move_garden

label shed:

    scene bg garden

    "C’est une cabane de jardin remplie d’un bordel INCOMMENSURABLE."

    "Si je fouille dans le bordel… cela me prendrait au moins 1 unité de temps."

    menu:
        "Fouiller":
            if not shears_inventory:
                $ shears_inventory = 1
                $ time_units -= 1
                "C’était une perte de temps, j’ai tout rangé, mais rien ne semble utilisable à part cette paire de cisailles."
            if shears_inventory == 2:
                "Tu croyais vraiment que j’allais retrouver des cisailles ?"

        "Ne pas fouiller":
            "Flemme."

    jump free_move_garden

label grave:

    scene bg garden

    "Voilà où repose papy..."

    if germaine_mission == 1 and not germaine_grave:
        "Il faut que je déterre la pauvre carcasse de mon grand-père..."

        menu:
            "À la main (3 unités de temps)":
                $ germaine_grave = True
                $ time_units -= 3
                "Je suis sale, j’ai mal aux mains, mais au moins c’est fait !"

            "Utiliser la pelle (1 unité de temps)" if shovel_inventory == 1:
                $ germaine_grave = True
                $ time_units -= 1
                $ shovel_inventory = 2
                "J’ai mal au bras, mais au moins papy peut respirer."

            "Ne pas déterrer":
                "Flemme."

    if germaine_grave:
        "… Je sais pas à quoi s’attendait mamie. Mais papy, avec sa vie (et son mariage) de martyre avec sa femme, c’était évident qu’il allait au paradis. Espérons que ces ossements suffisent à lui plaire."

    jump free_move_garden

label desk:

    scene bg library

    "C’est un bureau, il y a du papier et de quoi écrire dans les tiroirs"
    
    if abby_mission == 1 and not abby_weakness:
        "Bon… Je doit faire une liste de défauts à faire à la gloire et au caractère de merde de Léa. Le temps de tout lister j’en ai pour 3 unité de temps"

        menu:
            "Faire la liste (3 unités de temps)":
                $ abby_weakness = True
                $ time_units -= 3
                "Si jamais Léa tombe dessus, Je suis MORT."

            "Ne pas faire la liste":
                "Flemme."

    jump free_move_library

label cupboard:

    scene bg kitchen

    "Ce placard est fermé par une chaîne rouillé. C’est là où mamie mettait mais jouer confisqués car ‘dangereux’."

    if abby_mission == 1 and not abby_armament:
        "Il faut que je récupère tout l’armement de mon enfance pour Abby"

        menu:
            "Ouvrir à la main":
                "Jamais de la vie j’ouvre ça à main nue."

            "ouvrir avec la cisailles (1 unité de temps)" if shears_inventory:
                $ abby_armament = True
                $ time_units -= 1
                $ shears_inventory = 2
                "Je viens de niquer la cisaille, mais c’est ouvert !"

            "Ouvrir avec la pelle (1 unité de temps)" if shovel_inventory == 1:
                $ abby_armament = True
                $ time_units -= 1
                $ shovel_inventory = 2
                "Avec un bon coup avec la pelle, cela devrais être régler sans perdre du temps."
                "La pelle à rendu l’âme, tout comme la chaîne."

            "Ne pas ouvrir":
                "Flemme."
    if abby_armament:
        "Au moins elle ne pourras pas tuer Léa avec mes anciennes affaires, sauf si elle tape très fort avec les billes." 

    jump free_move_kitchen

label shovel:

    scene bg library

    if shovel_inventory == 0:
        "Une pelle ici ? Mais oui ! C’est ce qu’avait apporté Abby comme solution pour m’embrasser !"

        menu:
            "Prendre la pelle":
                $ shovel_inventory = 1
                "Parfait, cela pourra toujours servir."

            "Ne pas prendre la pelle":
                "flemme."
    
    if shovel_inventory != 0:
        "..."

        "Fait comme si tu ne la voyais pas. Tu l’as déjà prise je te rappelle."

    jump free_move_library

label trash:

    scene bg kitchen

    "C’est une poubelle, oui je suis très observateur."

    if germaine_mission == 1 and not germaine_trash:
        "Cela devrait me prendre 1 unité de temps de mettre le bordel à la poubelle."

        menu:
            " Nettoyer les déchets (1 unité de temps)":
                $ germaine_trash = True
                $ time_units -= 1
                "Eh bien… c’était pas si difficile en réalité, certes j’ai caché la moitié sous le tapis."

            "Ne pas nettoyer les déchets":
                "Flemme."

    jump free_move_kitchen

label oven:

    scene bg kitchen

    "Bien que ma grand-mère soit un fantôme, on dirait qu’elle fait toujours son passe-temps favori, engrosser les gens. Il y a des gâteaux tout chauds au four."

    menu:
        "Manger les gâteaux":
            $ time_units -= 2
            "Mmmmh~ j’ai pris une heur- deux unités de temps pour les manger, mais c’était bon !"

        "Ne pas manger les gâteaux":
            "Pas le temps de niaiser, j’ai un pipou à préserver !"

    jump free_move_kitchen

label bed:

    scene bg bedroom

    "Hum… Devrais-je dépenser une unité de temps en priant pour la consolidation de ma colonne vertébrale ?"

    menu:
        "OUI":
            $ time_units -= 1
            "Hideo Kojima, David Cage, Gabe Newell, Todd Howard, Peter Molyneux, Will Wright, Amy Hennig, Markus Persson, Sid Meier, Ewen Talleux, Shigeru Miyamoto et John Carmack.\n Sauvez ma saucisse de la tentation."

        "NON":
            "Je suis pas ENCORE dans la merde à ce point."

    jump free_move_bedroom

label ewen:

    scene bg bedroom

    "Ewen Talleux, mon développeur de jeux préféré !!"

    "C'est mon idole absolue, le dieu vivant du game design français."

    menu:
        "Lui parler de No Nut November":
            $ time_units -= 2
            "Ewen me regarde avec des yeux pleins de compassion."

            ew "Billy, mon garçon… tu es en train de faire une grave erreur."

            ew "Le No Nut November est un concept toxique qui promeut la répression des désirs naturels et sains du corps humain."

            ew "En tant que développeur de jeux vidéo, je t'encourage à embrasser ta sexualité de manière responsable et à ne pas te laisser influencer par des défis absurdes."

            ew "N'oublie pas que le véritable plaisir vient de l'acceptation de soi et du respect de ses propres besoins."

            "Je me sens… libéré."

        "Ne pas lui parler":
            "Flemme."

    jump free_move_bedroom