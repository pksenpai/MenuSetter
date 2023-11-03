from setter import call_menu
from typing import Tuple ##################### %%%%%%
import sys
import importlib #################################
import test001 #################################

def rm_parenthese(attribute):
    """ Remove parentheses for return pure data """
    return str(attribute).replace('(', '').replace(')', '')

class Core:
    TNT = tuple or non-tuple
    
    def __init__(self, module: str, args: TNT, className: str, attr: TNT):
        self.attribute = rm_parenthese(attr) if isinstance(attr, tuple) else attr
        self.className = className
        self.module = module
        self.args = rm_parenthese(args) if isinstance(args, tuple) else args
        self.obj = None
    
    def method_caller(self):
        for act in call_menu():
            if act == "exit":
                exit()
            # elif act == "back":
            #     sys.exit() # test
            else:
                yield act

    """
    ---------------------------------------------------------------------------
    """

    def module_caller(self):
        module_name = input('what is module name?>>> ')
        self.module = module_name

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
        Core.module_caller(self)
        Core.class_caller(self)
        
        
        if self.attribute:
            syntax = '{0}.{1}({2})'.format(self.module, self.className, self.attribute) # obj = ModuleName.ClassName(AttributesName)
        else:
            syntax = '{0}.{1}()'.format(self.module, self.className) # obj = ModuleName.ClassName()
        
        print("__________________________________")
        self.obj = eval(syntax)
        
        # self.obj = literal_eval(syntax) # have error why?!
        return self.obj
    