# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image cosmo neutre = "images/cosmo_neutre.png"
image cosmo angry = "images/cosmo_colere.png"
image abby neutre = "images/abby_neutre.png"
image abby angry = "images/abby_colere.png"
image germaine neutre = "images/germaine_neutre.png"
image germaine angry = "images/germaine_colere.png"

image bg car = "images/bg_car.jpg"
image bg bedroom = "images/bg_bedroom.jpg"
image bg garden = "images/bg_garden.jpg"
image bg hall = "images/bg_hall.jpg"
image bg library = "images/bg_library.jpg"
image bg kitchen = "images/bg_kitchen.jpg"

image nav = "images/nav.png"

# Déclarez les personnages utilisés dans le jeu.
define b = Character('Billy', color="#31cdfd")
define l = Character('Léa', color="#fde9a5")
define c = Character('Cosmo', color="#a8b977")
define a = Character('Abby', color="#d6767b")
define g = Character('Germaine', color="#ffba53")
define ew = Character('LE Ewen Talleux', color="#f54291")

transform rotate_25:
    rotate 25

# Variable pour suivre si l'action a été effectuée
default time_units = 11

default cosmo_mission = 0 # 0= première fois, 1= en cours, 2= terminée
default abby_mission = 0
default germaine_mission = 0

default cosmo_book = False
default cosmo_war = False
default abby_weakness = False
default abby_armament = False
default germaine_trash = False
default germaine_grave = False

default shovel_inventory = 0 # 0= pas dans l'inventaire, 1= dans l'inventaire, 2= cassée
default shears_inventory = 0