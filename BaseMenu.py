import importlib
from MenuSetter import call_menu
import test001
# from users import User


class MainMenu:
    def __init__(self, module, method, args, className, attribute):
        self.attribute = attribute
        self.attribute: str
        self.className = className
        self.module = module
        self.method = method
        self.args = args
        self.obj = None
    
    @staticmethod
    def show_menu() -> str:
        """method of menu_setter module, show menu and call action at end"""
        action = call_menu()
        print(action)
        return action 
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
        
        if self.attribute:
            obj_syntax_creator = '{0}.{1}({2})'.format(self.module, self.className, self.attribute) # obj = ModuleName.ClassName(AttributesName)
        # 
        else:
            obj_syntax_creator = '{0}.{1}()'.format(self.module, self.className) # obj = ModuleName.ClassName()
            
        self.obj = eval(obj_syntax_creator) 
        
        self.obj.show_name()
        # print(self.obj)
        # return self.obj
    
    def method_caller(self):
        self.method = self.show_menu()
        self.args = input('what is your argumants method?>>> ')
        return self.method, self.args
    """
    --------------------------------------------------------------------------
    """
    def class_caller(self):
        """ input class name """
        self.className = input('class name?>>> ')
        self.attribute = input('class attributes?>>> ')
        if self.className == 'Back' or self.attribute == 'Back':
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

        
# start_obj = Command() # ONE QUESTION : i didn't create object before, how call MenuSetter module without create class obj? **
# start_obj.connector()

"""
bugs: 
1.repeat menu in BaseMenu file # its fixed with commented line 108 and 109 that called class and created object but how?!
"""

""" TEST CALL"""
# def __init__(self, module, method, args, className, attribute):
obj1 = MainMenu('test001', None, None, 'test', None)
obj1.obj_caller()
