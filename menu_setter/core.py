from setter import call_menu
import importlib
import test001


class MainMenu:
    def __init__(self, module, method, args, className, attribute):
        self.attribute = attribute
        self.className = className
        self.module = module
        self.method = method
        self.args = args
        self.obj = None
    
    def method_caller(self):
        self.method = exit() if call_menu() == "exit" else call_menu() # call action from setter module if dont return exit command
        if self.method == "back":
            pass # go back
        self.args = input('what is your argumants method?>>> ')
        return self.method, self.args

    """
    ---------------------------------------------------------------------------
    """

    def module_caller(self):
        module_name = input('what is module name?>>> ')
        self.module = module_name
        # self.module = importlib.import_module(module_name) #BUGGGGGGGGGGGGGGGGGGGGGGGGG

    def class_caller(self):
        """ input class name """
        self.className = input('class name?>>> ')
        self.attribute = input('class attributes?>>> ')
        # if self.className == 'Back' or self.attribute == 'Back':
        #     connector.connect()

    """
    --------------------------------------------------------------------------
    """

    def obj_caller(self) -> object:
        """ 
        Call module, class and class attribute's from
        module_caller & class_caller method then Create an object 
        """
        MainMenu.module_caller(self)
        MainMenu.class_caller(self)
        
        if self.attribute:
            syntax = '{0}.{1}({2})'.format(self.module, self.className, self.attribute) # obj = ModuleName.ClassName(AttributesName)
        else:
            syntax = '{0}.{1}()'.format(self.module, self.className) # obj = ModuleName.ClassName()
        
        print(syntax)
        print("__________________________________")
        self.obj = eval(syntax)
        
        # self.obj = literal_eval(syntax) # have error why?!
        # self.obj.show_name() # from test001 module test001.test().show_name()
        return self.obj
    