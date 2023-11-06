from sys import argv


class test:
    def __init__(self, f_name, l_name, nickName, username, password):
        self.flag = True # it must be False by default but i defined it True because i cant signup in test 
        self.f_name = f_name
        self.l_name = l_name
        self.nickName = nickName
        self.username = username
        self.__password = password
        
    def signup(self):
        if self.flag == True:
            print("Actully you are in your account!!! XO")
            return 'menu_setter.core.back'
        
        else:
            while self.flag == False:
                cmd_username = input('enter an username>>> ')
                cmd_password = input('enter a password>>> ')
            print("Wellcome :D!!!\nsignup successfully!!!")
            
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
        
        return 'menu_setter.core.setTimer', 2
        # return 'menu_setter.core.setTimer' # this command missing 1 required positional argument(delay_time)
        # return 'menu_setter.core.stopMove'
        