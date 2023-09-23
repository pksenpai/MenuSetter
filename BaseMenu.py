import importlib
from MenuSetter import call_menu
# from users import User


class MainMenu:
    def __init__(self, module, method, args, __class, attribute) -> None:
        self.attribute = attribute
        self.attribute: str
        self._class = __class
        self.module = module
        self.method = method
        self.args = args
        self.obj = None
    
    @staticmethod
    def show_menu() -> str:
        """method of menu_setter module, show menu and call action at end"""
        action = call_menu() # type: ignore
        print(action)
        return action # type: ignore
    """
    ---------------------------------------------------------------------------
    """
    def module_caller(self):
        module_name = input('what is module name?>>> ')
        self.module = importlib.import_module(module_name)
        MainMenu.class_caller(self)

    def obj_caller(self) -> object:
        """ 
        Call class and class attribute's from
        class caller method & Create an object 
        """
        print('before obj')
        if not self.attribute:
            self.obj = getattr(self.module, (eval(self._class)())) # class Word -> class : obj = Word()
            return self.obj
        # obj = users.User(att)
        self.obj = eval(self._class)(self.attribute.split())
        # self.obj = getattr(self.module, eval(self._class))(map(str, self.attribute.split()))
        print(self.obj)
        return self.obj
    
    def method_caller(self):
        self.method = self.show_menu()
        self.args = input('what is your argumants method?>>> ')
        return self.method, self.args
    """
    --------------------------------------------------------------------------
    """
    def class_caller(self):
        """ input class name """
        self._class = input('class name?>>> ')
        self.attribute = input('class attributes?>>> ')
        if self._class == 'Back' or self.attribute == 'Back':
            Command.connector(self) # type: ignore

        MainMenu.obj_caller(self)


class Command(MainMenu):
    def __init__(self) -> None:
        pass
    
    def module_caller(self):
        return super().module_caller()

    def obj_caller(self) -> object:
        super().class_caller()
        return super().obj_caller()
    
    def method_caller(self):
        return super().method_caller()

    def connector(self):
        try:
            """ Call Action from Main Menu """
            method_str, args = self.method_caller()
            print(method_str)
            if method_str == 'Back' or args == 'Back':
                self.connector()

            """ Call Module and Create an object from class """
            self.module_caller()
            obj = self.obj_caller()
            method = getattr(obj, method_str)

            """ The method may have no arguments """
            if not args:
                method()
            else:
                method(args)
            
            """ Loop Menu """
            self.connector()

        except NameError as error:
            print(error)
        except ModuleNotFoundError as error:
            print(error)

        
start_obj = Command()
start_obj.connector()

"""
bugs: 
1.repeat menu in BaseMenu file
"""