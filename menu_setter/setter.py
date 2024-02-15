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
"""\____________________________[IMPORT MODULES]____________________________/"""
from ms_config import data_extractor
import os

"""\_________________________________[BODY]_________________________________/"""
class MenuSet:
    unactive_cmd_history: list = []
    hard_header: str = None
    
    def __init__(self, menu_instance:dict, header:str, space:str, active:bool = False):
        self.menu_instance = menu_instance
        self.cache_data: dict = None
        self.active_cmd_history: dict = None # %%%NEW%%% 0.1.4 bugfix
        self.last_header: str = None
        self.header: str = header
        self.space: str = space
        self.active: bool = active
        self.value: list = None
        self.action: dict = None
        self.cmd: int = None
        
    """\____________________________[INPUT METHODS]____________________________/"""
    
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
        self.__class__.hard_header = self.last_header
        self.last_header = self.header
        flag = None
    """\_______________________________[TOOLS]_______________________________/"""
    def indexing(self, print_options=True):
        if print_options:
            self.show_header(self.header) # menu header --> >Main Menu<
        
        self.cache_data = {}
        
        for num, option in enumerate(self.value, start=1):
            if print_options:
                """ <Separate title & sub:ACT|Sub_Option> """
                option : dict
                title = option.get("title") # title = title of option, sub = (ACTION or Another OPTION's)
                
                """ <Show Option's> """
                print(f'{self.space}|-> {num}-{title}')
            
            """ <Indexing: Set value option with index for easy act> """
            self.cache_data.setdefault(num, option)
        return num
    
    def run_cmd_history(self): # %%%NEW%%% 0.1.4 bugfix
        for cmd in self.active_cmd_history:
            num = self.indexing(print_options=False)
            self.menu_instance = self.cache_data.get(cmd)
            for key, value in self.menu_instance.items():
                if key == 'sub':
                    self.value = value
        self.header = self.__class__.hard_header
        return num
    
    """\____________________________[BODY METHODS]____________________________/"""
    def option_print(self):

        if self.active:
            self.active_cmd_history = self.__class__.unactive_cmd_history
            self.active = False
        else:
            if self.value: # if value of {sub: []} is empty go back 

                num = self.indexing()
                
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
        
        if self.active_cmd_history: # %%%NEW%%% 0.1.4 bugfix
            num = self.run_cmd_history()
            self.active_cmd_history = None
            self.option_print()
            
        """ <Command Input Func> """
        # self.__class__.unactive_cmd_history = [2, 4, 3, (2)--> last command]
        self.option_act()

        if self.cmd == num+1: # %%%NEW%%% 0.1.4 bugfix
            try:
                self.__class__.unactive_cmd_history.pop()
            except IndexError:
                print()
                print("ERROR: No previous page available! X3")
                print()
                self.option_print()
        else:
            self.__class__.unactive_cmd_history.append(self.cmd)
        
        """ <Fast EXIT> """
        if self.cmd == num+2:
            exit()

        """ <Go On option that user choosed> """
        self.menu_instance = self.cache_data.get(self.cmd)
        self.separator()

    """\____________________________[SEPARATOR]____________________________/"""

    def separator(self):
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
                    # TEST
                    # print('*'*10,'value:', value)
                    # print('*'*10,'instance:', self.menu_instance)
                    self.value = value
                    self.option_print()

    """\____________________________[DESIGNER METHODS]____________________________/"""
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
    active = False # 
    
    while True:
        menu_obj = MenuSet(menu_data, 'Main Menu', '\t', active=active) # processing data | display menu
        for act, header in menu_obj.separator(): # send data(act)
            if act == "back": # %%%NEW%%% 0.1.4 bugfix
                active = True
                break
            yield act, header

if __name__=='__main__':
    for act in call_menu():
        print(act)
