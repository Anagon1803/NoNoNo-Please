screen point_click_hall:

    imagemap:
        ground "bg hall"
        hotspot (1703, 201, 184, 651) action Jump("free_move_library")
        hotspot (814, 317, 406, 439) action Jump("free_move_garden")

    imagebutton:
        idle "nav"
        pos (33, 637)
        action Jump("free_move_kitchen")

    imagebutton at rotate_25:
        idle "nav"
        pos (108, 114)
        action Jump("free_move_bedroom")

    imagebutton:
        idle "abby neutre"
        pos (1248, 310)
        action Jump("abby_mission")

    imagebutton:
        idle "germaine neutre"
        pos (248, 374)
        action Jump("germaine_mission")

    imagebutton:
        idle "cosmo neutre"
        pos (914, 432)
        action Jump("cosmo_mission")

label free_move_hall:

    if time_units <= 0 or (cosmo_mission == 2 and abby_mission == 2 and germaine_mission == 2):
        jump check_end

    call screen point_click_hall

# =======================================================

screen point_click_library:

    imagemap:
        ground "bg library"
        hotspot (1451, 441, 140, 351) action Jump("shovel")
        hotspot (114, 96, 804, 453) action Jump("library")
        hotspot (580, 545, 780, 314) action Jump("desk")

    imagebutton:
        idle "nav"
        hover "nav"
        pos (84, 755)
        action Jump("free_move_hall")

label free_move_library:

    if time_units <= 0:
        jump check_end

    call screen point_click_library

# =======================================================

screen point_click_kitchen:

    imagemap:
        ground "bg kitchen"
        hotspot (424, 239, 141, 132) action Jump("cupboard")
        hotspot (770, 579, 377, 278) action Jump("oven")
        hotspot (0, 579, 225, 273) action Jump("trash")

    imagebutton:
        idle "nav"
        hover "nav"
        pos (33, 329)
        action Jump("free_move_hall")

label free_move_kitchen:

    if time_units <= 0:
        jump check_end

    call screen point_click_kitchen

# =======================================================

screen point_click_garden:

    imagemap:
        ground "bg garden"
        hotspot (1399, 388, 227, 232) action Jump("free_move_hall")
        hotspot (1544, 711, 374, 118) action Jump("flower_bed")
        hotspot (34, 323, 326, 254) action Jump("shed")
        hotspot (493, 414, 88, 123) action Jump("grave")

label free_move_garden:

    if time_units <= 0:
        jump check_end

    call screen point_click_garden

# ======================================================

screen point_click_bedroom:

    imagemap:
        ground "bg bedroom"
        hotspot (0, 478, 708, 421) action Jump("bed")
        hotspot (1422, 150, 332, 637) action Jump("free_move_hall")
        hotspot (1022, 118, 283, 297) action Jump("ewen")

label free_move_bedroom:

    if time_units <= 0:
        jump check_end

    call screen point_click_bedroom