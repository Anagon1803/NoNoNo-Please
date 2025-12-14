label intro_germaine:

    scene bg hall

    "Je déboule dans un couloir en courant, poursuivi par une ex morte et une bibliothèque qui me fait passer un bac de français accéléré."

    b "PUTAIN MAIS CALMEZ-VOUS"

    "Je glisse sur quelque chose par terre.\nUn vieux pull.\nMON vieux pull."

    "Je m’écrase comme une merde."

    b "…évidemment."

    "Un lent grincement résonne dans l’escalier juste à côté de moi.\nUn bruit que je connais trop bien.\nLe bruit du bois ancien… et du jugement."

    show germaine neutre at center 

    g "Voilà."

    "Je me fige."

    g "Voilà exactement pourquoi je suis morte."

    "Je me retourne très lentement."

    "Au sommet de l’escalier se tient une vieille dame translucide, en robe de chambre, bigoudis fantomatiques parfaitement en place, pantoufles flottantes.\nElle me regarde comme on regarde une erreur de la nature."

    b "Mamie… ?"

    g "GERMAINE."

    "Elle s’arrête sur une marche."

    "Elle me regarde de haut en bas, puis regarde le pull au sol."

    g "Tu sais…"

    "Elle sourit. Un sourire qui a tué des carrières et traumatisé des voisins."

    "C’est tout de même ce même sourire qui a fait en sorte que j’ai un daron."

    g "C’est à cause de TES affaires que je suis morte."

    "Je déglutis."

    b "Mamie, écoute, c’était un accident."

    g "CHUTE MORTELLE DANS LES ESCALIERS."

    "Elle lève un doigt spectral."

    g "À CAUSE D’UNE PAIRE DE CHAUSSETTES RIGIDES COMME DU CARTON."

    "Elle descend encore une marche.\nChaque pas résonne comme une condamnation."

    g "Et dois-je te RAPPELER de ce que tu as fait…"

    "Elle s’approche dangereusement."

    g "…LE LENDEMAIN DE MES FUNÉRAILLES ?"

    "Je ferme les yeux."

    g "…une soirée mousse."

    "Le silence."

    "Ho, je suis foutu, je suis mort."

    show germaine angry at center

    g "UNE."

    "Elle serre les poings."

    g "SOIRÉE."

    g "MOUSSE."

    g "DANS."

    g "MA."

    g "MAISON."

    "Les murs tremblent.\nDes cadres tombent.\nUn vase explose tout seul."

    g "T’AS FAIT DU BRUIT JUSQU’À L’AU-DELÀ !"

    "Elle hurle."

    g "J’ÉTAIS EN TRAIN DE SIGNER LES PAPIERS DE L’ENFER ET J’ENTENDAIS DU FRANCKY VINCENT !"

    b "C’ÉTAIT POUR ME REMONTER LE MORAL !"

    g "TU AS INVITÉ UN DJ DANS MON SALON, BILLY !"

    "Je tente de ramper en arrière."

    b "Mamie, s’il te plaît, je suis déjà en galère-"

    g "TU AS MIS DE LA MOUSSE"

    "Elle hurle encore plus fort."

    g "SUR MON BUFFET LOUIS XV."

    "Une des épées accrochées au mur se soulève toute seule derrière elle."

    b "Oh non non n-"

    g "JE VAIS TE TUER, BILLY."

    "Elle sourit."

    g "À cause de toi, je me suis énervée sur Satan ! Et j’ai perdu mes places VIP de l’enfer ! J’avais une superbe vue sur ton grand-père qui se faisait bouffer les couilles par Cerbère !"

    "L’épée vole.\nJe roule au sol.\nElle se plante dans le mur à dix centimètres de ma tête."

    b "OK ! OK ! J’AI ÉTÉ UN MAUVAIS PETIT-FILS !"

    g "Mauvais ?"

    "Elle se penche vers moi."

    g "TU ES UNE DÉCEPTION GÉNÉTIQUE."

    "Je me relève en courant."

    b "Je tiens de papa ! C’est pas de ma faute si ce dernier tient plus de grand-père que de toi !"

    "Je m’enfuis en tournant en rond dans le hall, entendant derrière moi la voix de Germaine hurler :"

    g "REVIENS ICI QUE JE T’APPRENNE À RANGER TES AFFAIRES, PETIT CON !"

    "Je cours aussi vite que je peux avec l’endurance d’une crevette asthmatique, pour finalement finir par atteindre l’autre escalier menant à l’étage."

    "..."

    "J’ai survécu ! Je suis un vrai Billy survivant !"

    "Tout cela grâce à ma technique extrêmement avancée qui s’appelle :"

    "La fuite."

    "Je finis par atteindre ma chambre."

    jump intro_bedroom

label germaine_mission:

    scene bg hall
    show germaine neutre at center 

    if germaine_mission == 0:
        "Vous savez quoi faire quand votre grand-mère veut votre peau ? Eh bien pas moi."
        
        "J’imagine que ça va être quitte ou double."
        
        g "Tu as quoi à me regarder comme ça avec tes yeux de merlan frit ? On va finir par comprendre que tu as aucune lueur d’intelligence !"
        
        "Je prends tout mon courage et je la charge de compliments. Faire gonfler son ego semble la meilleure tactique avec elle."
        
        g "Eh bien, je comprends pourquoi tu as une copine. Tu es assez fort pour faire de la lèche et manier ta langue."
        
        b "Je tiens ça de papy."
        
        g "Si seulement !"
        
        "Dégueulasse."
        
        g "Mais ces belles paroles ne sont pas suffisantes pour que je me laisse aller à t’aider."
        
        g "Tu vas devoir faire des choses pour ta grand-mère pour qu’elle veuille bien t’aider."
        
        b "C’est… c’est vraiment gentil de vouloir m’aider."

        show germaine angry at center
        
        g "Ta gueule oui ! Je fais surtout ça pour pas avoir à t’entendre couiner quand elle te pliera la BIT-"
        
        b "AH ÇA VA ! C’EST BON J’AI COMPRIS !"

        $ germaine_mission = 1
    
    if germaine_mission == 1:
        g "Bon écoute-moi bien petit garnement, tu as des tâches à faire."

        if not germaine_trash:
            g "Tu vas devoir ranger cette maison ! Il y a des piles de MERDIER PARTOUT. Va prendre la poubelle dans la cuisine et faire le tour de la maison."
        
        if germaine_trash:
            g "Eh bien, je suis impressionné que tu aies pu faire une tâche ménagère."

        if not germaine_grave:
            g "Tu vas déterrer ton grand-père ! Il est hors de question que je m’occupe de toutes les tâches ici alors que ce dernier se la coule douce dans sa tombe !"
        
        if germaine_grave:
            g "Bravo pour avoir sorti ton grand-père de sa sieste ! Évidemment, ce tas d’os ne veut pas bouger, c’est moi qui fais tout dans cette baraque !"
        
        if germaine_trash and germaine_grave:
            $ germaine_mission = 2

    if germaine_mission == 2:
        g "Cela t’a pris 25 ans, mais tu as enfin bougé ton cul pour faire quelque chose dans cette baraque !"

    jump free_move_hall