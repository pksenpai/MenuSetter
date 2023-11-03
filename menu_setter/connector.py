from core import Core


def message_back(msg, core):
    """ message back from outer codes """ 
    if msg == 'menu_setter.core.back':
        connect(core)

def connect(core):
    """ Call Action from Main Menu """
    for methodName, args in core.method_caller():
        try:
            if methodName == 'back': # its back to first of menu page %%%BUG%%%
                connect(core)
            
            """ Create an object from class """
            obj = core.obj_caller()
            method = getattr(obj, methodName)
            
            """ The method may have no arguments """
            if not args:
                message = method()
            else:
                message = method(*args)

            if message: # if message back from outer code's response the defined request's
                message_back(message, core)
            
        except NameError as error:
            print(error)
        except ModuleNotFoundError as error:
            print(error)



        
""" TEST CALL"""
# 1-attribute, 2-argument, 3-module, 4-className
core_obj = Core(('Parsa', 'Ahmadian', 'PKPY', 'pk', '123'), (':D', 21), 'test001', 'test')
connect(core_obj)
