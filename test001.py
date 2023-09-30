from sys import argv


class test:
    def __init__(self):
        self.flag = False
        self.f_name = "Parsa"
        self.l_name = "Ahmadian"
        self.nickname = "PKPY"
        
    def signup(self):
        cmd_password: str
        while self.flag == False or cmd_password.lower() != "back":
            cmd_password = argv
            if cmd_password == 123:
                self.flag = True
                return "Password is correct"
            print('password is incorrect')
            
    def show_name(self):
        if self.flag == True:
            print(f"_____________________________________________________\n"
                f"My fullname is {self.f_name} {self.l_name}\n" 
                f"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n"
                f"My nickname is {self.nickname}\n"
                f"_____________________________________________________")
            return True
        print("--you need to sign up first!!!")
        