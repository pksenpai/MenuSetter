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


class menu_center:
    def __init__(self, menu_instance, header, space) -> None:
        self.menu_instance = menu_instance
        self.header = header
        self.space = space
        self.value = None
        self.action = None
        self.cmd = None
        

    def option_act(self):
        print('__________________')
        self.cmd = int(input('cmd?>>> '))
        return self.cmd

    def option_print(self):
        cash_data = {}
        for num, option in enumerate(self.value, start=1): # type: ignore
            """ <Separate title & sub:ACT|Sub_Option> """
            option : dict
            title = option.get("title") # title = title of option, sub = (ACTION or Another OPTION's)
            
            """ <Show Option's> """
            print(f'{self.space}|-> {num}-{title}')
            
            """ <Set value option with index for easy act> """
            cash_data.setdefault(num, option) 

        print(f'{self.space}|-> {num+1}-Back') 
        print(f'{self.space}|-> {num+2}-Exit') 

        """ <Command Input Func> """
        num_option = self.option_act()

        """ <Go On option that user choosed> """
        self.menu_instance = cash_data.get(num_option)
        self.menu_print()


    def menu_print(self):
        self.menu_instance: dict

        for key, value in self.menu_instance.items():
            if key == 'title': # --> v1 = 'Login' v2 = 'login' v3 = sub...
                """ <Show Menu Header> """
                self.header = value # save header value
                print('__________________')
                print(f'>{self.header}<')
            
            elif key == 'act':
                if isinstance(value, str):
                    self.action = value
                    return self.action
            else:
                """ set UI space """
                menu_shape.menu_UI
                """ <Show Menu Option> """
                self.value = value
                self.option_print()


class menu_shape(menu_center):
    def __init__(self, menu_instance, header, space) -> None:
        super().__init__(menu_instance, header, space)

    def menu_print(self):
        return super().menu_print()
    
    def open_data(self):
        file_path = path.join('config', 'input.json') # data file address

        with open(file_path) as data_menu_json:
            self.menu_instance = load(data_menu_json)
        print('data extracted successfuly!')
        self.menu_print()
        return self.action

    def menu_UI(self):
        """ <UI Setting> """
        header_size = len(self.header)
        self.space = ' ' * ((header_size+2) // 2)

def call_menu():
    start_loop = menu_shape(None, 'Main Menu', '\t')
    action = start_loop.open_data()
    return action

print(call_menu())
