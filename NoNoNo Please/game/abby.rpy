label intro_abby:

    scene bg hall

    "Je claque la porte du hall et m’appuie dessus, essoufflé, comme si Cosmo allait traverser le mur pour me faire un exposé sur la biodiversité de mon slip."

    "Je sens la porte trembler."

    scene bg library
    
    "Dans la panique, je me mets à fuir dans la salle la plus proche de moi, la bibliothèque ! Grâce à mon talent rare pour la lâcheté, je parcours les quelques mètres sans me faire de point de côté."

    b "Ok, bon, respire Billy, juste deux jours… deux… petits… jours…"

    "Une brise glacée me frôle la nuque.\nUne voix se glisse dans mon oreille comme une chanson d’ascenseur possédée."

    show abby neutre at center with fade

    a "Alors on revient à la maison… Billy ?"

    "Je me fige. Non. NON. PAS MAINTENANT. PAS ELLE."

    "Une silhouette apparaît lentement devant moi, flottant à dix centimètres du sol comme si la gravité était une suggestion."

    "Une jeune femme en tenue de servante d’époque, tablier transparent, cheveux attachés parfaitement, expression… meurtrière."

    b "A… Abby…"

    "Elle croise les bras."

    a "Bah alors, Billy… ça fait longtemps, dis donc."

    "Elle avance en planant."

    a "Quoi ? Pas content de revoir ton amoureuse décédée ?"

    "Je tente un sourire maladroit."

    b "Abby, écoute… c’est compliqué, je-"

    a "NON."

    "Elle lève une main."

    a "On va pas commencer avec ton “c’est compliqué”. La dernière fois que tu as dit ça, tu m’as LITTÉRALEMENT larguée en disant que nos “fluides n’étaient pas compatibles”."

    "Je me frappe mentalement. Mais quel CON que je suis !"

    b "C’était… une mauvaise formulation."

    a "Une mauvaise formulation ?"

    "Elle plisse les yeux."

    a "Tu m’as quitté parce que tu pouvais pas me toucher."
    
    "Elle pointe un doigt spectral sur mon torse."

    a "T’AS ROMPU POUR RAISON DE COLLISION PHYSIQUE IMPOSSIBLE."

    "Je lève les bras."

    b "Bah c’est vrai ! C’est important, quand même !"
    
    "Elle me pousse. Enfin, elle traverse mon torse, mais l’intention y était."

    a "Je t’aimais, moi ! On se tenait la main en mettant trois heures pour que ça marche sans problème ! On regardait des films ensemble même si je passais au travers du canapé !"

    "Elle se rapproche, les yeux brillants d’un mélange d’émotion et d’envie de meurtre."

    a "Et toi… tu m’as larguée parce que tu pouvais pas me rouler une pelle !"

    b "Hé, c’est plus complexe que ça !"

    "Elle souffle si fort que ça fait trembler les meubles."

    "Prions pour qu’elle ne se rende pas compte qu’elle peut me frapper avec un livre."

    a "Alors explique-moi… pourquoi tu es ici ?"

    "Je me frotte le visage."

    b "…Je fuis ma copine."

    a "Oh."

    "Elle sourit lentement, comme quelqu’un qui vient d’apprendre qu’il existe un enfer encore plus profond que celui où elle est."

    a "Tu fuis… ta copine ?"

    b "Oui."

    "Je baisse les yeux. Et malheureusement, elle apprend vite, je me prends ses Robert dans la tronche."

    "…"

    "…"

    "Les dictionnaires Robert."

    "L’impact dans mon visage n’est pas le même d’un coup."

    b "AIE ! Ça fait mal, bordel !"

    a "C’est le principe d’un bouquin dans la gueule, connard !"

    "Des livres commencent alors à sortir des étagères pour m’apporter en pleine gueule les bienfaits de la littérature."

    "Heureusement, bouger des objets semble beaucoup la fatiguer. Elle a du mal à me toucher avec Guerre et Paix pour mon plus grand bonheur. Je profite de cette faiblesse pour m’enfuir dans le hall à nouveau." 

    jump intro_germaine

label abby_mission:

    scene bg hall
    show abby neutre at center with fade

    if abby_mission == 0:
        "Je m’approche avec beaucoup de crainte d’Abby."
        
        "Avec de la chance, elle détesteras ma copine plus qu’elle ne me déteste moi." 
        
        a "Que me veux mon ex pas encore décédé de ma main ?"
        
        "Je passe alors quelque longues seconde à m’excuser, et a lui dire que c’était ma faute et pas la sienne." 
        
        b "Elle veut… euh… enfin… elle veut faire ce qu’on ne pouvait pas faire, toi et moi, tu vois ?"
        
        "Un ange passe, disons plutôt un spectre passif-agressif."
        
        "…"
        
        a "BILLY. TU TE FOUS DE MOI."
        
        b "NON ! C’est juste... C’est le No Nut November et je d-"
        
        "Elle hurle de rire."
        
        a "T’AS QUITTÉ UNE FANTÔME PARCE QUE TU POUVAIS PAS BAISER. ELLE, ELLE LE PEUX ET MAINTENANT TU TE BARRES POUR NE PAS LE FAIRE !!!"
        
        "L’ironie est palpable."
        
        a "Mais tu est un CONNARD."
        
        "Elle tourne autour de moi en volant."
        
        a "Et le pire, c’est que je suis sûre qu’elle est super mignonne, ta copine. Hein ? Elle est mignonne ?"
        
        b "Très."
        
        a "Grosse poitrine ?"
        
        a "Abby !"
        
        a "Pardon. C’était juste professionnel de ma part."
        
        "Elle s’arrête devant moi, bras derrière le dos, l’air faussement innocente."
        
        a "Je vais t’aider."
        
        b "Hein ?"
        
        "Elle glisse son doigt fantôme sur mon torse en mode ‘je règne ici’."
        
        a "Je ne vais PAS laisser une vivante te toucher alors que MOI, j’ai jamais pu !"
        
        a "C’est à moi de faire échouer ta vie amoureuse !"
        
        b "C’est… pas rassurant."
        
        "Elle claque des doigts. Comme pour me rappeler a l’ordre."
        
        a "Allez, viens Billy. On va te garder pur comme un moine jusqu’au 1er décembre."
        
        b "Tu me fais peur."
        
        a "C’est littéralement mon boulot maintenant."

        $ abby_mission = 1
    
    if abby_mission == 1:
        a "On va devoir ce préparer pour l’accueillir"

        if not abby_weakness:
            a "Je veux une liste complète de ses faiblesses et de ses défauts. Il faut que je connaisse mon adversaire. La liste des défauts c’est juste de l’égo, je veux qu’on soit d’accord sur le fait que je suis meilleure."
        
        if abby_weakness:
            a "Cette liste de défaut est vraiment énorme ! Je suis sur de gagner une joute verbale avec elle maintenant."

        if not abby_armament:
            a "Il me faut également de l’armement ! Bon ont est pas en Amérique donc compte pas sur les flingues. A la place du doit m’apporter tout ce qu’il y a de dangereux dans le placard fermé de la cuisine."
        
        if abby_armament:
            a "Pétard, punaises et même pistolet a plomb ! Parfait, je vais lui faire une putain de guerre comme elle en a jamais vue." 
        
        if abby_weakness and abby_armament:
            $ abby_mission = 2

    if abby_mission == 2:
        a "Je suis armée et motivée. Tu peux allez te cacher dans la chambre je la retiendrais."

    jump free_move_hall