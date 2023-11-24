"""\______________________________DEFAULT MENU______________________________/"""
def json_data():
    default_menu={
            "title": "Main Menu",
            "act": None,
            "sub": [
                    {"title": "Login",
                    "act": {
                        "M": "test001",
                        "F": "login",
                        "args": [":D", 22],
                        "C": "test",
                        "attr": ["Parsa", "Ahmadian", "PKPY", "pk", "123"]
                    },
                    "sub": [
                            {"title": "Edit Profile",
                                "act": None,
                                "sub": [
                                        {"title": "Change Username",
                                        "act": "change_username",  
                                        "sub": None},
                    
                                        {"title": "Change Password",
                                        "act": "change_password",
                                        "sub": None}     
                                    ]},

                            {"title": "Contacts Panel",
                                "act": None,
                                "sub": [
                                        {"title": "Add New Contact",
                                        "act": "add_contact",
                                        "sub": None}
                                    ]}     
                            ]},

                    {"title": "SignUp",
                    "act": {
                        "M": "test001",
                        "F": "signup",
                        "C": "test",
                        "attr": ["Parsa", "Ahmadian", "PKPY", "pk", "123"]
                    },
                    "sub": [
                            {"title": "Show Name",
                                "act": None,
                                "sub": None}
                            ]},
                    
                    {"title": "documents",
                    "act": {
                        "print": "https://github.com/pksenpai/MenuSetter"
                    },
                    "sub": [
                            {"title": "author",
                                "act": {
                                    "print": "Parsa Ahmadian(PKPY)"
                                },
                                "sub": None}
                            ]}
                    ]
            }

    return default_menu

"""\______________________________IMPORT MODULE______________________________/"""
from .setter import call_menu
from ms_config import data_extractor, extra_opt
from pprint import pprint
from json import dumps
from shutil import copytree
from os import path
import argparse

"""\______________________________ARGPARSE______________________________/"""

parser = argparse.ArgumentParser(
                    prog='menu-commander',
                    description='commands for ms',
                    epilog='')

"""\____________________________MAIN VARIABLE___________________________/"""

parser.add_argument(
    'command',
    choices=[
        'ms-init', 
        'ms-show', 
        'ms-call'
    ]
)


"""\____________________________INIT OPTIONS____________________________/"""

parser.add_argument(
    '-n', '--name', 
    help='set a custom name for your menu header(default-name: >Main Menu<)'
) 
parser.add_argument(
    '-j', '--json',
    action='store_true',
    help='init a json file if ms-config directory exist'    
)

"""\____________________________SHOW OPTIONS____________________________/"""

parser.add_argument('-v', '--verbose', action='store_true', help='show more menu details') # on/off flag

#===========================================================
args = parser.parse_args() # access to arguments           =
#===========================================================

"""\____________________________USEFUL FUNCS____________________________/"""

def generate_json_file(PATH, FILE, EXT):
    filePath = '{}/{}.{}'.format(PATH, FILE, EXT)
    if not path.isfile(filePath):
        menu = json_data()
        menu_name='Main Menu'
        if args.name: # give a custom name to menu name as menu header
            new_name = args.name # new name
            menu_name = new_name
            menu["title"] = new_name
                        
        json_pf = dumps(menu, indent=4) # pretty formatter
        if menu:
            with open(filePath, 'w+') as json_file: # create file with site and doc link near other ms_config files
                json_file.write(json_pf)
                
        return f'{FILE}.{EXT} file added!:D\nmenu name: {menu_name}'
    else:
        return f'{FILE}.{EXT} already EXIST!:o'

def read_extra_opt():
    PATH = extra_opt.menu_config_path
    FILE = extra_opt.menu_config_fileName
    EXT = extra_opt.menu_config_fileExtension
    return PATH, FILE, EXT

def read_json(): # read menu.json
    return data_extractor.menu_ext()
    
"""\________________________________BODY________________________________/"""

###\____________FUNCS____________/###
def init_menuSetter(): # default name ==> main menu    
    PATH, FILE, EXT = read_extra_opt()

    if args.json:
        result = generate_json_file(PATH, FILE, EXT) 
        
    elif not path.isdir(PATH):
        """ Copy config files to parent_directory """
        current_dir = path.abspath(path.dirname(__file__))
        source_dir = path.join(current_dir, PATH)
        new_configFile_name = PATH
        
        copytree(source_dir, new_configFile_name) # copying...
        _, menu_name = generate_json_file(PATH, FILE, EXT)
                
        result = f'NICE: menu-setter files generated successfuly as >{menu_name}< :D'
        
    else:
        error=(f"{PATH} directory is already EXIST!:o" 
               f"\nif you want to init a json file for menu input"
               f"\nuse '-j' after 'ms-init' :3")
        result = error
    
    return result
    
def show_menuSetter():
    # display menu with command
    menu = read_json()
    oneline_menu = menu # %%%ONELINE_SHOW%%% in dev
    if args.verbose:
        # show more about menu options
        verbose_menu = menu
        return verbose_menu
        
    return oneline_menu

def call_menuSetter():
    # move in menu with command
    for act in call_menu():
        if args.verbose:
            print(act)
        else:
            print(end="\r")

try: 
    ###\_____________CALL____________/###
    if args.command == "ms-init": # create config files <-- start with this command
        print(init_menuSetter())

    elif args.command == "ms-show":
        pprint(show_menuSetter()) 

    # if open('connector.py', 'r'): # its mean menu has been inited with init-ms command
    elif args.command == "ms-call":
        call_menuSetter()

    else:
        print("this command is NOT EXIST!:(\n"
              "use this command '[python/python3] menu-setter [-h][--help]' :)")

except FileNotFoundError:
    print("ms-config or ms-config/*.json is NOT EXIST!:("
          "\nuse this command: '[python/python3] menu-setter ms-init'"
          "\nfor create config files|")
