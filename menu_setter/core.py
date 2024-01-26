"""\_________________________IMPORT MODULES________________________/"""
from .setter import call_menu
from .exceptions import Core_except as exception
from importlib import import_module as _import_
from ast import literal_eval
import os

"""\__________________________EXTRA TOOLS__________________________/"""
def import_module(module_name):
    result = _import_(module_name)
    return result

def rm_parenthese(myList):
    """ Convert tupel to str & remove parentheses """
    myString = str(myList).replace('[', '').replace(']', '')
  
    """ convert str to pure object """
    return literal_eval(myString) # more SAFE <-- recommended!!!
    # return eval(myString) # more FAST


"""\_____________________________BODY______________________________/"""
    # Core processing the custom menu from input to pure code & make
    # an object to call your project methods after every get action
    # commands from setter 

class Core:

    def __init__(self, moduleName: str, func: str, args: tuple, className: str, attr: tuple):
        self.module = import_module(moduleName) if moduleName else None
        
        self.function = func
        self.argument = rm_parenthese(args)
        
        self.className = className
        self.attribute = rm_parenthese(attr)
        
        self.content = None
        self.header = None
        self.obj = None
    
    def method_caller(self):
        for act, self.header in call_menu():
            
            if isinstance(act, dict):
                """\_____________Print_____________/"""
                self.content = act.get("print")
                
                """\____________Module____________/""" # import ModuleName
                module = act.get("M"); print(module)
                self.module = import_module(module) if not self.module and module else self.module 
                """\____________Class____________/"""
                className = act.get("C"); print(className)
                self.className = className if className else self.className
                """\______Attr______/"""
                attr = act.get("attr"); print(attr)
                self.attribute = rm_parenthese(attr) if attr else self.attribute# convert list to str
                
                """\____________Func____________/"""
                function = act.get("F"); print(function)
                self.function = function if function else self.function
                """\______Args______/"""
                args = act.get("args"); print(args)
                self.argument = rm_parenthese(args) if args else self.argument # convert list to str
                
            elif act == "back":
                self.function, self.argument = "back", None
                
            elif act == "exit": # %%%CHECK%%%
                exit()
            else:
                # raise exception.wrong_act_type(act)
                print(f"'{act}' is not a dict!\n'{act}' must be in dict! XO")
                
            
            yield self.function, self.argument # method(args)

    def obj_caller(self) -> object:
        """ 
        Create an object : obj = ModuleName.ClassName(AttributesName)
        """
        if self.content or self.module:
            print(f"\n _______________/{self.header}\_______________",
                "\n/                " + (" "*len(self.header)) + "                \\")
        
        if self.content:
            print(self.content)

        if self.module:
            if self.className: # if class exists
                core_object = getattr(self.module, self.className) # obj = ModuleName.ClassName()
            
                if self.attribute: # if attr exists|
                    self.obj = core_object(*self.attribute) # obj = Module.Class(Attributes)
                else:
                    self.obj = core_object() # obj = Module.Class()
            
                return self.obj, 'c'
                    
            if self.function: # if class NOT exists|(Only function base!)
                self.obj = getattr(self.module, self.function)
                return self.obj, 'f'
        
        else:
            return False, None
    