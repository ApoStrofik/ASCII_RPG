import random

from game_class import *
from monster_class import *
from gui import *
import time

niveau = Niveau()
base_monster = Monster()
monster_lvl = []


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

    def reset_screen():
        clear_terminal()
        upper_winpart(player_class, player_class.name, player_class.classNAME, player_class.level)

    if len(monster_lvl) <= 0:

        clear_terminal()
        print(monster_lvl)
        time.sleep(2)

        niveau.lvl += 1

        for levels in range(niveau.lvl):
            monster_choice = random.randint(1, 2)

            if monster_choice == 1:
                skeleton = Skeleton()
                monster_lvl.append(skeleton)
            if monster_choice == 2:
                wolf = Wolf()
                monster_lvl.append(wolf)

        start_adventure()

    else:
        reset_screen()

        menu(("MARCHAND", "SAC A DOS", "COMBAT"))
        print("")
        choice = int(input(Fore.GREEN + "Votre choix : " + Fore.RESET))

        while True:
            try:
                if choice == 1:
                    pass
                elif choice == 2:
                    print(player_class.items_bag)
                    break
                elif choice == 3:

                    reset_screen()
                    in_fight = True

                    while in_fight:
                        print(f"Un {monster_lvl[0].name} vous attaque !!!")
                        menu(("ATTAQUE", "SAC A DOS"))
                        in_fight_choice = int(input(Fore.GREEN + "Votre choix : " + Fore.RESET))

                        if in_fight_choice == 1:
                            pass
                        elif in_fight_choice == 2:
                            pass

                        in_fight = False
                        start_adventure()

            except ValueError:
                start_adventure()



