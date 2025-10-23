from game_class import *
from monster_class import *
from gui import *
import time


def start_menu():
    clear_terminal()
    header("ASCII RPG par ApoStrofik")
    menu(["COMMENCER", "SORTIE"])
    print("")

    while True:
        try:
            choice = int(input(Fore.GREEN + "Votre choix : " + Fore.RESET))
            if choice == 1:
                player_config()
                break
            elif choice == 2:
                clear_terminal()
                print("\n\n\n")
                header("AU REVOIR")
                print("\n\n\n")
                time.sleep(2)
                exit()
            else:
                clear_terminal()
                start_menu()
                break
        except ValueError:
            clear_terminal()
            start_menu()
            break


def player_config():
    global player_name

    clear_terminal()
    header("DEBUT DE L'AVENTURE")
    print("")
    name_choice = str(input(Fore.GREEN + "Choisissez un nom : " + Fore.RESET))

    if len(name_choice) == 10:
        player_name = name_choice
    elif len(name_choice) < 10:
        player_name = name_choice + (10 - len(name_choice)) * " "
    else:
        print("\n")
        print(Fore.LIGHTRED_EX + "10 caractères MAX" + Fore.RESET)
        time.sleep(2)
        player_config()

    fonc_class_choice()


def fonc_class_choice():
    global player_class

    clear_terminal()
    header("CHOIX DE LA CLASSE")
    print("")
    menu(["GUERRIER", "MAGE", "VOLEUR"])
    print("")

    while True:
        try:
            class_choice = int(input(Fore.GREEN + "Choisissez votre classe : " + Fore.RESET))
            chosen_class = class_choice

            if chosen_class == 1:
                player_class = Warrior(player_name, 50, 50, 25, 10, 5, 200)
                start_adventure()
                break
            elif chosen_class == 2:
                player_class = Mage(player_name, 50, 50, 5, 10, 25, 200)
                start_adventure()
                break
            elif chosen_class == 3:
                player_class = Rogue(player_name, 50, 50, 10, 25, 5, 200)
                start_adventure()
                break
            else:
                clear_terminal()
                fonc_class_choice()
        except ValueError:
            clear_terminal()
            fonc_class_choice()


def start_adventure():

    def upper_winpart():
        header(f"{player_class.name} {player_class.classNAME} de niveau {player_class.level}")
        print("")
        player_infos(player_class)
        print("\n")

    def fight():
        clear_terminal()
        upper_winpart()

        print("Un " + Back.WHITE + Fore.BLACK + f"{monster_lvl[0].name}" + Style.RESET_ALL + " vous attaque !")
        print("")
        menu(("ATTAQUER", "COMPETENCES", "SAC A DOS"))
        print("")
        choice = int(input(Fore.GREEN + "Votre choix : " + Style.RESET_ALL))


    lvl = 0

    skeleton = Skeleton()
    wolf = Wolf()
    monster_list = [skeleton, wolf]
    monster_lvl = []

    while player_class.life > 0:

        if len(monster_lvl) <= 0:

            lvl += 1

            for level in range(lvl):
                monster_lvl.append(monster_list[random.randint(0, len(monster_list) - 1)])

        else:
            fight()

