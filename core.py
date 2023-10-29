import importlib
from MenuSetter import call_menu


class MainMenu:
    def __init__(self, module, method, args, className, attribute):
        self.attribute = attribute
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
