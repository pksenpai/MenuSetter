from core import MainMenu
import test001



def connect(self):
    try:
        """ Call Action from Main Menu """
        method_str, args = core.method_caller()
        print(method_str)
        if method_str == 'Back' or args == 'Back':
            connect()

        """ Call Module and Create an object from class """
        core.module_caller()
        obj = core.obj_caller()
        method = getattr(obj, method_str)

        """ The method may have no arguments """
        if not args:
            method()
        else:
            method(args)
        
        """ Loop Menu """
        connect()

    except NameError as error:
        print(error)
    except ModuleNotFoundError as error:
        print(error)

        
""" TEST CALL"""
# def __init__(self, module, method, args, className, attribute):
core = MainMenu('test001', None, None, 'test', None)
connect(core)
