from sys import argv


class test:
    def __init__(self):
        self.flag = True # just for now its True for texting but next time must change to False
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
            
    def login(self, name='PKPY'):
        user = input('username: ')
        passw = input('password: ')
        if passw == '123':
            if self.flag == True:
                print(
                    f"login success!!!\n"
                    f"Welcome {name}:D"
                )
                return True
        print("--you need to sign up first!!!")


# def printt():
#     for i in range(5):
#         input()
#         yield i



# for j in printt():
#     print(j)
# def test(*args):
#     print(str(args))

# test(1)