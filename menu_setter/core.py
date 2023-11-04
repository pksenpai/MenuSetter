"""\__________________________IMPORT MODULES__________________________/"""
from setter import call_menu
from typing import Tuple ##################### %%%%%%
import importlib 
from ast import literal_eval


"""\__________________________EXTRA TOOLS__________________________/"""

def rm_parenthese(attribute):
    """ Convert tupel to str & remove parentheses """
    myString = str(attribute).replace('(', '').replace(')', '')
    
    """ convert str to pure object """
    return literal_eval(myString) # more SAFE <-- recommended!!!
    # return eval(myString) # more FAST

"""\__________________________BODY CLASS__________________________/"""

class Core:
    TNT = tuple or non-tuple
    
    def __init__(self, attr: TNT, arg: TNT, module: str, className: str):
        self.attribute = rm_parenthese(attr) if isinstance(attr, tuple) else attr # convert tuple to str
        self.argument = rm_parenthese(arg) if isinstance(arg, tuple) else arg # convert tuple to str
        self.module = importlib.import_module(module) # import ModuleName 
        self.className = className
        self.obj = None
    
    def method_caller(self):
        for act in call_menu():
            if act == "exit":
                exit()
            yield act, self.argument # if act command is not 'exit' return action & argument's method

    def obj_caller(self) -> object:
        """ 
        Call module, class and class attribute's from
        module_caller & class_caller method then Create an object 
        """
        
        core_object = getattr(self.module, self.className) # obj = ModuleName.ClassName()|create an object
        
        if self.attribute: # if attr exist|
            self.obj = core_object(*self.attribute) # obj = ModuleName.ClassName(AttributesName)
        else:
            self.obj = core_object() # obj = ModuleName.ClassName()
            
        tester = "Login"
        print(f" _______________/{tester}\_______________",
               "\n/                " + (" "*len(tester)) + "                \\")
        
        return self.obj

        #===============================================================================#
        """ stored temporary previous code's """
        # if self.attribute: # obj = ModuleName.ClassName(AttributesName) <-- attr exist|
            # syntax = '{0}.{1}{2}'.format(self.module, self.className, self.attribute) 
        # else:
            # syntax = '{0}.{1}()'.format(self.module, self.className)

        # self.obj = eval(syntax)
        # self.obj = literal_eval(syntax) # have error why?!! %%%QUESTION%%%
        #===============================================================================#


