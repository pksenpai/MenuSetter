"""
exmple:
>main menu<
    |-------- Login
    |           |----- admin
    |           |----- user
    |
    |-------- SignUp
                |----- user
"""
"""
{"title": "main menu",
 "act": None,
 "sub": [
		{"title": "Login", --> show menu option to user
		 "act": "login", --> call login method in module that connected to basemenu
         "sub": [                 | --> go to next step
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
				 "act": None
                 "sub": [
                        {"title": "Add New Contact",
				         "act": "add_contact",
                         "sub": None},
                         ...
                         .
                         .
                        ]}     
				]},

		{"title": "SignUp",
		"sub": "user_signup"}
		]}

"""
from json import load
from os import path


class MenuSet:
    def __init__(self, menu_instance, header, space) -> None:
        self.menu_instance = menu_instance
        self.header = header
        self.space = space
        self.value = None
        self.action = None
        self.cmd = None
        

    def option_act(self):
        print('__________________')
        self.cmd = int(input('cmd?>>> ')) # CHOOSE OPTION FROM MENU

    def option_print(self):
        cache_data = {}
        for num, option in enumerate(self.value, start=1): # type: ignore
            """ <Separate title & sub:ACT|Sub_Option> """
            option : dict
            title = option.get("title") # title = title of option, sub = (ACTION or Another OPTION's)
            
            """ <Show Option's> """
            print(f'{self.space}|-> {num}-{title}')
            
            """ <Set value option with index for easy act> """
            cache_data.setdefault(num, option) 

        cache_data.setdefault(num+1, {"title": "Back", "act": "back", "sub": None})
        print(f'{self.space}|-> {num+1}-Back') 
        cache_data.setdefault(num+2, {"title": "Exit", "act": "exit", "sub": None})
        print(f'{self.space}|-> {num+2}-Exit')

        """ <Command Input Func> """
        self.option_act()
        
        """ <Fast EXIT> """
        if self.cmd == num+2:
            exit()
            
        """ <Go On option that user choosed> """
        self.menu_instance = cache_data.get(self.cmd)
        self.menu_print()
        print('im in last of line in option_print')


    def menu_print(self):
        self.menu_instance: dict
        print('im in menu_print func')
        while True:
            for key, value in self.menu_instance.items():
                if key == 'title': # --> v1 = 'Login' v2 = 'login' v3 = sub...
                    """ <Show Menu Header> """
                    self.header = value # save header value
                    print('__________________')
                    print(f'>{self.header}<')
                
                elif key == 'act':
                    if value: # change from isinstance(value, str)
                        self.action = value
                        print(value)
                        yield self.action
                        # print(self.header)
                else:
                    """ set UI space """
                    self.menu_UI()
                    """ <Show Menu Option> """
                    self.value = value
                    self.option_print()

    def menu_UI(self):
        """ <UI Setting> """
        header_size = len(self.header)
        self.space = ' ' * ((header_size+2) // 2)


def call_menu():
    file_path = path.join('config', 'input.json') # data file address

    with open(file_path) as data_menu_json:
        data = load(data_menu_json)
    print('___________________________')
    print('data extracted successfuly!')

    menu_obj = MenuSet(data, 'Main Menu', '\t')
    for act in menu_obj.menu_print():
        yield act


#********************************#
# """ <for TEST setter MODULE> """
# for action in call_menu():
#     print(action)
#********************************#
