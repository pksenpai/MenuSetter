from core import Core


def connect(core):
    """ Call Action from Main Menu """
    for methodName in core.method_caller():
        try:
            if methodName == 'back': # its back to first of menu page %%%BUG%%%
                connect(core)
            args = None # just dont forget args
            """ Create an object from class """
            obj = core.obj_caller()
            method = getattr(obj, methodName)

            """ The method may have no arguments """
            if not args:
                method()
            else:
                method(args)
        
        except NameError as error:
            print(error)
        except ModuleNotFoundError as error:
            print(error)



        
""" TEST CALL"""
# 1-module, 2-args, 3-className, 4-attribute
core_obj = Core('test001', None, 'test', None)
connect(core_obj)
