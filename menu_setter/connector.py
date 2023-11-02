from core import MainMenu


def connect(core):
    """ Call Action from Main Menu """
    for methodName, args in core.method_caller():
        try:
            # method_name, args = core.method_caller() # 4Example: method_name, args = print, "Hello World!"
            # print(method_name)
            # if method_name == 'Back' or args == 'Back':
            #     connect()

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

    """ Loop Menu """
    connect(core)


        
""" TEST CALL"""
# object = CoreClassName(moduleName, methodName, args, className, attribute)
core_obj = MainMenu('test001', None, None, 'test', None)
connect(core_obj)
