'''
{
'parsa' : {'password' : 123, 'contact_id' : 1 },
'abolfazl' : {'password' : 123, 'contact_id' : 2 },
}
'''
# update : hello name 
# update conect user emails together
# menu setter login --> change
# update : password palisty

'''
1- show all contact
2- save all contact
3- read all contact
4- after login sync to user class contact
'''
"""
{
    username1 : {
                    password_user1 : 123
                    contact_id : 1        
                }
    ...
}
"""
# import file soon... 


class User :

    id = 0
    dict_user = {}




    def __init__(self, x) -> None:
        username, \
        password = x

        self.user_name = username
        self.password = password
        User.id += 1
        self.id = User.id
        self.flag = False

    
    def __str__(self) -> str:
        return f'hey this user {self.user_name} with password {self.password} added!!!'    

    def signup(self):
        if self.user_name in User.dict_user:
            return 'username does already exist'
        else :
            User.dict_user[self.user_name]= {
                                                'password' : self.password,
                                                'contact_id' : self.id
                                            }
            self.flag = True
            file.save_file(User.dict_user)
    


    def login(self) :
        result = file.read_file()
        if self.user_name in result :
            if self.password == result.get(self.user_name)['password'] :
                self.flag = True
                return 'Welcome to your acount!'
            return 'password is wrong!'
        return 'this username not exist!'
        

    def change_username(self, new_username):
        if self.flag :
            users_data = file.read_file()
            users_data : dict
            
            username_value = users_data[self.user_name]
            users_data.pop(self.user_name)
            new_data = users_data

            new_data.setdefault(new_username, username_value)
            self.user_name = new_username
            file.save_file(new_data)
            
            return new_data
        return 'for change username you must login!'
    

    def change_password(self, new_password):
        if self.flag :
            users_data = file.read_file()
            users_data: dict
            
            new_data = users_data
            new_data[self.user_name]['password'] = new_password
            self.password = new_password
            file.save_file(new_data)
            
            return new_data
        return 'for change password you must login!'

