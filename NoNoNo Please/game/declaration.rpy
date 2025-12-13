# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image cosmo neutre = "images/cosmo_neutre.png"
image abby neutre = "images/abby_neutre.png"
image germaine neutre = "images/germaine_neutre.png"

# Déclarez les personnages utilisés dans le jeu.
define b = Character('Billy', color="#fde9a5")
define l = Character('Léa', color="#fde9a5")
define c = Character('Cosmo', color="#a8b977")
define a = Character('Abby', color="#d6767b")
define g = Character('Germaine', color="#ffba53")

transform resize_char:
    zoom 0.7
    ypos 1300

transform resize_bg:
    xysize(config.screen_width, config.screen_height)  # Prend la taille de l'écran

# Variable pour suivre si l'action a été effectuée
default nb_jour = 0
default pause_count = 0
default win = 0

default max_sanite = 100
default max_satiete = 100
default max_camp = 3

default sanite = 100
default satiete = 100
default camp = 3