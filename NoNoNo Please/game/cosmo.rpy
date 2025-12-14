label intro_cosmo:

    scene bg garden

    "Je viens à peine de garer la voiture devant le portail que quelque chose me frappe : le jardin\nEnfin… ce qu’il reste du jardin. On dirait une jungle tropicale qui a décidé de se mettre en grève."

    "Même les plantes ont des revendication de gilet jaune !"

    "Je fais trois pas dans l’herbe, et soudain une fumée verte (oui, VERTE) s’élève du sol."

    show cosmo neutre at center with fade

    c "Héééééé mec… tu peux faire attention à mes vibes ? Tu marche sur mes cousine là !"

    "Je sursaute en ratant un battement de cœur."

    "Devant moi, un type apparaît en translucide, avec un chapeau de paysan, des tongs fantomatiques et un veste qui flotte dans un vent imaginaire."

    "Il tient un énorme joint spectral qui crépite littéralement comme une bûche de cheminée."

    b "…Cosmo ?"

    "Le fantôme lève les yeux au ciel comme si je venais de prononcer le mot interdit."

    c "Ouais, BROOOO… Cosmo. Celui dont tu as anéanti TRENTE-TROIS plants de beuh en jouant au foot dans MON jardin, tu t’en souviens ?"

    "Il tire une latte, la fumée forme un panneau « INTERDIT AUX GOSSES DE MERDE »."

    b "Écoute, j’étais jeune (bien que je le soit toujours), et c’était le jardin de MA grand-mère je te r-"

    c "Jeune ? JEUNE ?! Mec, t’étais une catastrophe écologique ambulante !"

    "Il ce met à compter sur ses doigts :"

    c "Tu roulais en scooter 50 qui fumait plus que moi, tu jetais des canettes dans les buissons, et t’avais une empreinte carbone tellement haute que même les glaciers pleuraient ton nom, frangin."
    
    b "C’est exagéré quand même…"

    "Cosmo s’approche, passe au travers d’un buisson, puis revient AVEC un vieux emballage de chips."

    c "Ça, Billy. Ça, c’est marqué 2009 dessus. C’est toi. Je le SAIS. Je me souviens du dédain que tu avais quand tu le jetais dans les PÉTUNIA !"

    c "LES PÉTUNIA BILLY !"

    b "Je t’arrête tout de suite, j’ m’en branle."

    c "…"

    b "…"

    c "…"

    "Cosmo me dévisage, puis son expression change.\nLe type sourit. Mais en même temps, il était parfaitement terrifiant. On dirais qu’il viens de débrancher et brancher son cerveau."

    b "Ok pardon j’aurais pas du dire ça… je… je suis grave stressé d’accord ? Je doit survire à ma meuf là !"

    c "Attend mec… t’as une meuf ? TOI ? HA ! Faut croire que la vie trouve toujours un chemin, même s’il mène à un attardé mental. Moi qui pensais que j’étais le seul défoncé dans les environs, faut que je rencontre ta copine."

    "…"

    "C’est vexant"

    c "Bref et pourquoi tu l’as fuit enfaîte ? Tu lui as aussi brisé le cœurs a cette pauvre plante ?"

    b "C’est pas le moment et pas le sujet. Et de toute manière tu comprendrais pas le problème !"

    c "Ah ouais je peux pas comprendre ? Laisse moi deviner… ont est le 28…"

    c "Tu veux survivre à ta meuf… et réussir ton No Nut November ?"

    "Il expire une volute de fumée en forme de “Bonne chance”."

    b "Tu sais ce que c’est que le NNN ? Je savais pas que les fantômes avais le câble."

    c "Non, j’ai la 5G sur mon ectophone."

    "Lui et ses putain de calembour !"

    b "Bref dans tout les cas, c’était vraiment pas agréable de te revoir. Je vais te laisser ensemencer les fleurs avec ton ectoplasme et j-"

    c "Ouais c’est plus naturel quand c’est fait main."

    b "… Je veux VRAIMENT pas savoir Cosmo…"
    
    "Et sans lui laisser le temps de répondre une autre connerie, je m’enfuis dans le hall du manoir."

    jump intro_abby

label cosmo_mission:

    scene bg hall
    show cosmo neutre at center with fade

    if cosmo_mission == 0:
        "Je m’approche de Cosmo, avec un peu de confiance."

        "Après tout c’est un mec comme moi, il devrait comprendre."

        c "Toi t’as un truc à me demander, et je sens que ça va pas me plaire bro."

        "Je passe alors quelques brèves minutes à m’excuser, et à lui expliquer que je suis qu’une merde. Cette dernière chose est facile à lui faire avaler."

        c "Bro… tu vas avoir besoin de moi. Et ça, ça vaut beaucoup plus que quelques excuses."

        "Je déglutis."

        "Cosmo flotte devant moi, bras croisés, l’air d’un gourou prêt à bénir ou maudire."

        c "On va faire un marché, Billy."

        b "Quel genre de marché… ?"

        c "Simple : tu m’aides à “sauver la planète” dans le manoir… et je t’aide à ne pas te faire attraper par ta copine en chaleur."

        b "Du coup… t’es… avec moi ?"

        c "Non, mec. Je suis avec la Terre, mais tu viens en bonus."

        $ cosmo_mission = 1
    
    if cosmo_mission == 1:
        c "Voilà ce que tu dois faire."

        if not cosmo_book:
            c "Tu dois me trouver un livre bro ! Marguerite, ma fleur de compagnie qui me sert de compagne, ne peut pas dormir sans une bonne histoire. Trouve-moi un exemplaire de ‘La Phytophilie chez les elfes sylvains’."
        
        if cosmo_book:
            c "Parfait pour le livre ! Ma copine est une vraie plante de culture. Mec, je suis sûr que ça va lui plaire."

        if not cosmo_war:
            c "Il y a aussi une guerre entre la République des tulipes et l’État facho des mauvaises herbes. Faut que tu traites le problème à la racine. Et avant que tu demandes pourquoi je le fais pas moi, je suis un pacifiste."
        
        if cosmo_war:
            c "C’est triste… mais c’était la bonne chose à faire. Espérons que les mauvaises herbes n’auront pas de nouveau chancelier dans les prochains jours." 
        
        if cosmo_book and cosmo_war:
            $ cosmo_mission = 2

    if cosmo_mission == 2:
        c "T’inquiète mon frère, t’es béni des fleurs désormais !"

    jump free_move_hall