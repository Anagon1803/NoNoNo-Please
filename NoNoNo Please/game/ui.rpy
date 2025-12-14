screen hud_time_units():

    # Le HUD est au-dessus de tout
    zorder 100
    layer "overlay"

    frame:
        xalign 0.02
        yalign 0.03
        padding (16, 12)
        background Solid("#000000AA")  # Noir semi-transparent
        # corner_radius 12

        vbox:
            spacing 6

            # Titre
            text "Temps restant" size 20 color "#ffffff"

            # Ligne valeur + icône
            hbox:
                spacing 8

                text "⏳" size 22
                text "[time_units]" size 22 color (
                    "#ff5555" if time_units <= 3 else
                    "#ffcc55" if time_units <= 6 else
                    "#fde9a5"
                )

            # Barre de temps
            bar:
                value AnimatedValue(time_units, range=11, delay=0.2)
                xmaximum 220
                ymaximum 11
                left_bar Solid("#fde9a5")
                right_bar Solid("#444444")