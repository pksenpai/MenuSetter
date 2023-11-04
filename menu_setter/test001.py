from sys import argv
import core

class test:
    def __init__(self, f_name, l_name, nickName, username, password):
        self.flag = True # it must be False by default but i defined it True because i cant signup in test 
        self.f_name = f_name
        self.l_name = l_name
        self.nickName = nickName
        self.username = username
        self.__password = password
        
    def signup(self):
        cmd_password: str
        while self.flag == False or cmd_password.lower() != "back":
            cmd_password = argv
            if cmd_password == 123:
                self.flag = True
                return "Password is correct"
            print('password is incorrect')
            
    def login(self, emoji: str, age: int):
        """ <check user & password for login> """
        
        user = input('username: ')
        input_password = input('password: ')
        
        print('input:', input_password)
        print('input:', type(input_password))

        print('stored:', self.__password)
        print('stored:', type(self.__password))
        
        if user == self.username and input_password == self.__password:
            if self.flag == True:
                print(
                    f"login success!!!\n"
                    f"Welcome {self.f_name} {self.l_name} "
                    f"with age {age} & nickname {self.nickName} {emoji}"
                )
                
        elif user == self.username:
            print("WARNING: --your username is wrong!!!")
            return 'menu_setter.core.back'
        else:
            print("WARNING: --your password is wrong!!!")
            return 'menu_setter.core.back'
        
        return 'menu_setter.core.setTimer'
        # return 'menu_setter.core.stopMove'
        
