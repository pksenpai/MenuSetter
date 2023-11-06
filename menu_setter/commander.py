import argparse

parser = argparse.ArgumentParser(
                    prog='cms',
                    description='commands for ms',
                    epilog='')

"""\____________________________MAIN VARIABLE____________________________/"""

parser.add_argument('cms') # positional arg

"""\____________________________INIT OPTIONS____________________________/"""

# optional that takes a value
parser.add_argument('-n', '--name', 
                    help='set a custom name for your menu(default-name: >Main Menu<)'
                ) 

"""\____________________________CALL OPTIONS____________________________/"""

parser.add_argument('-v', '--verbose', action='store_true') # on/off flag

#===========================================================
args = parser.parse_args()
#===========================================================



"""\________________________________BODY_______________________________/"""

###\_____________FUNCS____________/###
def init_menu():
    default_name = 'Main Menu'
    menu_name = default_name

    if args.name: # give a custom name to menu name as menu header
        new_name = args.name
        menu_name = new_name
    
    
    return f'NICE: menu-setter files generated successfuly as >{menu_name}< :D'
    
def call_menu():
    # call menu with command
    if args.verbose:
        pass # explain more about options
    return


###\_____________CALL_____________/###
if args.cms == "init-ms": # create config files <-- start with this command
    print(init_menu())

# if open('connector.py', 'r'): # its mean menu has been inited with init-ms command
#     if args.cms == "call-ms":
#         print(call_menu())
