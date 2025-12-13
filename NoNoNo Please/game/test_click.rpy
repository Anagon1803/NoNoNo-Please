# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Images pour le système point & click
image bg room = "room.jpg"  # Remplacez par votre image de fond
image item key = "key.png"  # Image pour un objet cliquable
image item door = "door.png"  # Image pour une porte

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

# Écran pour le système point & click
screen point_click_room:

    # Bouton image pour un objet (clé)
    imagebutton:
        idle "item key"
        hover "item key"  # Vous pouvez avoir une image différente pour hover
        pos (300, 400)  # Positionnez selon votre image
        action Jump("pickup_key")

    # Bouton image pour une porte
    imagebutton:
        idle "item door"
        hover "item door"
        pos (600, 200)
        action Jump("open_door")

# Le jeu commence ici
label test:

    # Ajouter l'arrière-plan
    scene bg room
    with fade

    e "Je me fige.\nNon.\nNON.\nPAS MAINTENANT.\nPAS ELLE."

    # Appeler l'écran point & click
    call screen point_click_room

label pickup_key:
    e "Vous avez ramassé une clé !"
    # Ici, vous pouvez ajouter du code pour gérer l'inventaire
    jump start  # Retour à l'écran, ou continuer l'histoire

label open_door:
    e "Vous ouvrez la porte avec la clé."
    # Transition vers une nouvelle scène
    jump next_scene

label next_scene:
    e "Vous entrez dans la pièce suivante."
    # Ajoutez plus d'histoire ici
    return
