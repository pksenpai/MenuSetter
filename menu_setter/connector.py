from core import MainMenu


def connect(core):
    try:
        """ Call Action from Main Menu """
        method_name, args = core.method_caller() # 4Example: method_name, args = print, "Hello World!"
        # print(method_name)
        # if method_name == 'Back' or args == 'Back':
        #     connect()

        """ Create an object from class """
        obj = core.obj_caller()
        method = getattr(obj, method_name)

        """ The method may have no arguments """
        if not args:
            method()
        else:
            method(args)
        
        """ Loop Menu """
        connect(core)

    except NameError as error:
        print(error)
    except ModuleNotFoundError as error:
        print(error)

        
""" TEST CALL"""
# object = CoreClassName(moduleName, methodName, args, className, attribute)
core_obj = MainMenu('test001', None, None, 'test', None)
connect(core_obj)
