from colorama import *
import os

def clear_terminal():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def header(text):
    char = "-"
    print(Fore.RED + ((len(text) + 10) * char) + Fore.RESET)
    print(Fore.RED + "-" + Fore.RESET + f"    {text}    " + Fore.RED + "-" + Fore.RESET)
    print(Fore.RED + ((len(text) + 10) * char) + Fore.RESET)

def menu(menu_items_list):
    list = menu_items_list
    item_num = 1

    print("")
    for items in list:
        print(Fore.RED + f"{item_num} " + Fore.RESET + f"{items}")
        item_num += 1

def player_infos(player_obj):

    if player_obj.life >= (player_obj.max_life / 3) * 2:
        color = Fore.GREEN
    elif player_obj.life < (player_obj.max_life / 3) * 2 and player_obj.life >= player_obj.max_life / 5:
        color = Fore.YELLOW
    else:
        color = Fore.RED

    print(Back.WHITE + Fore.BLACK + f"EXP" + Style.RESET_ALL + " : " + Back.GREEN + (int(player_obj.experience / 10) * " ") + Style.RESET_ALL + (
            (10 - int(player_obj.experience / 10)) * "_") + "   " + color + f"{player_obj.life} " + Style.RESET_ALL + f"/ {player_obj.max_life} PV" +
          "   " + f"{player_obj.gold}" + Fore.YELLOW + " ©" + Style.RESET_ALL)

def upper_winpart(player_obj, player_name, class_player, player_lvl):
    header(f"{player_name} {class_player} de niveau {player_lvl}")
    print("")
    player_infos(player_obj)
    print("\n")