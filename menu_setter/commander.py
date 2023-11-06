from setter import call_menu
from ms_config import data_extractor
from pprint import pprint
import argparse


parser = argparse.ArgumentParser(
                    prog='cms',
                    description='commands for ms',
                    epilog='')

"""\____________________________MAIN VARIABLE____________________________/"""

parser.add_argument('command') # positional arg

"""\____________________________INIT OPTIONS____________________________/"""

# optional that takes a value
parser.add_argument('-n', '--name', 
                    help='set a custom name for your menu header(default-name: >Main Menu<)'
                ) 

"""\____________________________CALL OPTIONS____________________________/"""

parser.add_argument('-v', '--verbose', action='store_true', help='show more details') # on/off flag

#===========================================================
args = parser.parse_args()
#===========================================================



"""\________________________________BODY_______________________________/"""

###\____________FUNCS____________/###
def init_menuSetter():
    default_name = 'Main Menu'
    menu_name = default_name

    if args.name: # give a custom name to menu name as menu header
        new_name = args.name
        menu_name = new_name
    
    
    return f'NICE: menu-setter files generated successfuly as >{menu_name}< :D'
    
def show_menuSetter():
    # display menu with command
    menu = data_extractor.menu_ext()
    oneline_menu = menu # %%%ONELINE_SHOW%%% in dev
    if args.verbose:
        # show more about menu options
        verbose_menu = menu
        return verbose_menu
        
    return oneline_menu

def call_menuSetter():
    # call menu with command
    for act in call_menu():
        if args.verbose:
            print(act)
        else:
            print(end="\r")

    
###\_____________CALL____________/###
if args.command == "init-ms": # create config files <-- start with this command
    print(init_menuSetter())

elif args.command == "show-ms":
    pprint(show_menuSetter()) 

# if open('connector.py', 'r'): # its mean menu has been inited with init-ms command
elif args.command == "call-ms":
    call_menuSetter()
