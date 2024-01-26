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
 "act": null, 
 "sub": [
		{"title": "Login", ==> show header option to user
		 "act": {            ==> call module, method with arguments, class with attributes
			"M": "test001",
			"F": "login",
			"args": [":D", 22],
			"C": "test",
			"attr": ["Parsa", "Ahmadian", "PKPY", "pk", "123"]
		 },
         "sub": [                  ==> go to next step
				{"title": "Edit Profile",
				 "act": null,      ==> no action
                 "sub": [
						{"title": "Change Username",
					 	 "act": null,
                         "sub": null}, ==> last option in menu
	
						{"title": "Change Password",
					 	 "act": null,
                         "sub": null}     
					]},

				{"title": "Contacts Panel",
				 "act": null
                 "sub": [
                        {"title": "Add New Contact",
				         "act": null,
                         "sub": null},
                         ...
                         .
                         .
                        ]}     
				]},

		{"title": "SignUp",
		"sub": ...}
		]}

"""
"""\____________________________IMPORT MODULES____________________________/"""
from ms_config import data_extractor
import os

"""\_________________________________BODY_________________________________/"""
class MenuSet:
    unactive_cmd_history = []
    
    def __init__(self, menu_instance, header, space) -> None:
        self.menu_instance = menu_instance
        self.cache_data = None
        self.active_cmd_history = [] # %%%NEW%%% 0.1.4 bugfix
        self.last_header = None
        self.header = header
        self.space = space
        self.value = None
        self.action = None
        self.cmd = None
        
    """\____________________________INPUT METHODS____________________________/"""
    
    def option_act(self):
        flag = False
        while flag==False:
            try:
                print(' ______________________________')
                print('/')
                self.cmd = int(input('\_Select the option number>>> ')) # CHOOSE OPTION FROM MENU
                if len(self.cache_data) < self.cmd:
                    print()
                    print(f'ERROR: this [{self.cmd}- ] option is NOT EXIST!!! :O')
                    print()
                    
                else:
                    flag = True
            except ValueError:
                print()
                print("ERROR: Your request is incorrect, please enter a number! :(")
                print()
        flag = None

    """\____________________________BODY METHODS____________________________/"""

    def option_print(self):
        
        if self.value: # if value of {sub: []} is empty go back 
            self.show_header(self.header) # menu header --> >Main Menu<
            self.last_header = self.header
            self.cache_data = {}
            for num, option in enumerate(self.value, start=1):
                """ <Separate title & sub:ACT|Sub_Option> """
                option : dict
                title = option.get("title") # title = title of option, sub = (ACTION or Another OPTION's)
                
                """ <Show Option's> """
                print(f'{self.space}|-> {num}-{title}')
                
                """ <Set value option with index for easy act> """
                self.cache_data.setdefault(num, option)
                
            """ <Set value option with index for back & exit options> """ 
            self.cache_data.setdefault(num+1, {"title": "Back", "act": "back", "sub": None})
            print(f'{self.space}|-> {num+1}-Back') 
            self.cache_data.setdefault(num+2, {"title": "Exit", "act": "exit", "sub": None})
            print(f'{self.space}|-> {num+2}-Exit')
            
        else:
            self.show_header(self.last_header) # menu header --> >Main Menu<
            for num, option in enumerate(self.cache_data.values(), start=1):
                # print('=================')
                # print(option)
                # print('=================')
                """ <Separate title & sub:ACT|Sub_Option> """
                option : dict
                title = option.get("title") # title = title of option, sub = (ACTION or Another OPTION's)
                
                """ <Show Option's> """
                print(f'{self.space}|-> {num}-{title}')
        
        print('@_________________') # menu footer --> @____________...
        

        """ <Command Input Func> """
        # self.__class__.unactive_cmd_history = [2, 4, 3, (2)--> last command]
        def run_cmd_history(): # %%%NEW%%% 0.1.4 bugfix
            for index, cmd in enumerate(self.active_cmd_history):
                yield index, cmd
            
        if self.active_cmd_history: # %%%NEW%%% 0.1.4 bugfix
            for index, cmd in run_cmd_history:
                self.cmd = cmd
                self.active_cmd_history.pop(index)
                self.menu_instance = self.cache_data.get(self.cmd)
                self.menu_print()
        else: # %%%NEW%%% 0.1.4 bugfix
            if self.cmd: 
                self.__class__.unactive_cmd_history.append(self.cmd)
            self.option_act()

        if self.cmd == num+1: # %%%NEW%%% 0.1.4 bugfix
            try:
                self.__class__.unactive_cmd_history.pop()
                self.active_cmd_history = self.__class__.unactive_cmd_history
            except IndexError:
                print()
                print("ERROR: No previous page available! X3")
                print()
                self.option_print()
        
        """ <Fast EXIT> """
        if self.cmd == num+2:
            exit()

        """ <Go On option that user choosed> """
        self.menu_instance = self.cache_data.get(self.cmd)
        self.menu_print()

    """\____________________________DIVIDER____________________________/"""

    def menu_print(self):
        self.menu_instance: dict
        
        while True:
            for key, value in self.menu_instance.items():
                if key == 'title':
                    self.header = value # save header value
                
                elif key == 'act':
                    if value:
                        self.action = value # save action value
                        yield self.action, self.header
                else:
                    """ set UI space """
                    if value:
                        self.menu_UI(self.header)
                    else:
                        self.menu_UI(self.last_header)
                        
                    """ <Show Menu Option> """
                    self.value = value
                    self.option_print()

    """\____________________________DESIGNER METHODS____________________________/"""
    @staticmethod
    def show_header(header):
        """ <Display Menu Header> """
        print('@_________________')
        print(f'>{header}<')
    
    def menu_UI(self, header):
        """ <UI Setting> """
        header_size = len(header)
        self.space = ' ' * ((header_size+2) // 2)


#=======================================================================================#
###\__________________________________CONNECTOR_____________________________________/###

def call_menu():# | data_extractor --data--> SETTER --data--> CORE |
    print('\n>===============================================@')
    menu_data = data_extractor.menu_ext() # get data
    menu_data: dict
    
    menu_obj = MenuSet(menu_data, 'Main Menu', '\t') # processing data | display menu
    
    for act, header in menu_obj.menu_print(): # send data(act)
        act: dict
        yield act, header

if __name__=='__main__':
    for act in call_menu():
        print(act)
