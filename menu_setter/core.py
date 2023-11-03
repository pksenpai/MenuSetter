"""\__________________________IMPORT MODULES__________________________/"""
from setter import call_menu
from typing import Tuple ##################### %%%%%%
import sys
import importlib #################################
import test001 
from ast import literal_eval


"""\__________________________EXTRA TOOLS__________________________/"""

def rm_parenthese(attribute):
    """ Convert tupel to str & remove parentheses """
    myString = str(attribute).replace('(', '').replace(')', '')
    return eval(myString) # convert str to pure object


"""\__________________________BODY CLASS__________________________/"""

class Core:
    TNT = tuple or non-tuple
    
    def __init__(self, module: str, arg: TNT, className: str, attr: TNT):
        # self.attribute = rm_parenthese(attr) if isinstance(attr, tuple) else attr # convert tuple to str
        self.module = module
        self.argument = rm_parenthese(arg) if isinstance(arg, tuple) else arg # convert tuple to str
        self.className = className
        self.attribute = attr
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
        
        if self.attribute:
            syntax = '{0}.{1}{2}'.format(self.module, self.className, eval(str(self.attribute))) # obj = ModuleName.ClassName(AttributesName)
        else:
            syntax = '{0}.{1}()'.format(self.module, self.className) # obj = ModuleName.ClassName()
        
        print("__________________________________")
        self.obj = eval(syntax)
        
        # self.obj = literal_eval(syntax) # have error why?!!
        return self.obj
    